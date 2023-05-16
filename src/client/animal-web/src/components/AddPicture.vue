<template>
    <div class="vl-parent" ref="main_container">
      <div class="container">
        <input type="file" ref="fileInput" @change="handleFileUpload" accept="image/*" />
        <div v-if="selectedImage" class="image-container">
          <img :src="selectedImage" alt="Selected Image" />
        </div>
        <div class="description-container">{{ prediction }}</div>
        <div class="buttons-container">
          <button @click="handleOK">OK</button>
          <button @click="handleCancel">Cancel</button>
        </div>
        <form v-if="prediction !== null" @submit="submitForm">
          <label for="predictionCorrect">Is the prediction correct?</label>
          <select id="predictionCorrect" v-model="predictionCorrect">
            <option value="yes">Yes</option>
            <option value="no">No</option>
          </select>
          <label for="trueLabel">True Label:</label>
          <input type="text" id="trueLabel" v-model="trueLabel" required>
          <button type="submit">Submit</button>
        </form>
      </div>
    </div>
  </template>
  
  <script>
  import axios from "axios";

  export default {
    
    data() {
      return {
        selectedImage: null,
        uploadedImage: null,
        prediction: null,
        predictionCorrect: null,
        trueLabel: '',
      };
    },

    methods: {
      handleFileUpload(event) {
        const file = event.target.files[0];
        if (file) {
          const reader = new FileReader();
          reader.onload = () => {
            this.selectedImage = reader.result;
          };
          reader.readAsDataURL(file);
          this.uploadedImage = file;
        }
      },

      handleOK() {
        let loader = this.$loading.show({
          color: "#16fa97",
          loader: "dots",
          height: 128,
          width: 128,
          lockScroll: true,

          container: this.fullPage ? null : this.$refs.main_container,
          canCancel: false,
          onCancel: this.onCancel,
        });

        console.log("OK button clicked");

        const formData = new FormData();
        formData.append("image", this.uploadedImage);

        axios.post("http://localhost:5000/predict", formData)
        .then(response => {
          console.log(response.data);

          this.prediction = response.data[0]['label'];
          this.predictionCorrect = null;

          loader.hide();
        })
        .catch(error => {
          console.log(error);
          loader.hide();
        });


      },

      submitForm() {
        event.preventDefault();
        const formData = new FormData();
        formData.append("image", this.uploadedImage);
        formData.append("predicted_label", this.prediction);
        formData.append("true_label", this.trueLabel); // Replace "true_label_value" with the actual true label value
        formData.append("description", "description_value"); // Replace "description_value" with the actual description value
        formData.append("time", new Date().toISOString());

        axios
          .post("http://localhost:5000/feedback", formData)
          .then((response) => {
            console.log("Feedback submitted:", response.data);
            // Handle any further actions after submitting the feedback
          })
          .catch((error) => {
            console.log("Error submitting feedback:", error);
            // Handle the error scenario, if needed
          });

      },

      handleCancel() {
        this.selectedImage = null;
        this.uploadedImage = null;
        console.log("Cancel button clicked");
      },

      onCancel() {
        console.log("onCancel");
      },
    },
  };
  </script>


<style scoped>
.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 20px;
}

input[type="file"] {
  margin-bottom: 20px;
}

.image-container {
  margin-bottom: 20px;
  text-align: center;
  max-width: 800px;
  max-height: 800px;
}

img {
  max-width: 100%;
  height: auto;
}

.buttons-container {
  display: flex;
  justify-content: center;
}

button {
  margin: 0 10px;
  padding: 10px 20px;
  background-color: #4CAF50;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s;
}

button:hover {
  background-color: #45a049;
}

button:focus {
  outline: none;
}

</style>