<template>
    <div class="container">
      <input type="file" ref="fileInput" @change="handleFileUpload" accept="image/*" />
      <div v-if="selectedImage" class="image-container">
        <img :src="selectedImage" alt="Selected Image" />
      </div>
      <div class="description-container"> Tukaj bo opis</div>
      <div class="buttons-container">
        <button @click="handleOK">OK</button>
        <button @click="handleCancel">Cancel</button>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        selectedImage: null,
        uploadedImage: null,
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
        // Handle OK button click
        // You can access the uploaded image file using 'this.uploadedImage'
        // You can perform any necessary actions with the image here
        console.log("OK button clicked");
      },
      handleCancel() {
        // Handle Cancel button click
        // You can reset the selected image and perform any necessary cleanup here
        this.selectedImage = null;
        this.uploadedImage = null;
        console.log("Cancel button clicked");
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