<template>
    <div class="w-50 m-auto" ref="main_container">
        <h1>Petster 2000</h1>
        <p class="text-left">
            Welcome to our website dedicated to the wonderful world of home pets! Here, you can unleash the power of
            artificial intelligence to learn more about your furry companions. Our innovative platform allows you to upload
            a photo of your beloved pet and receive a tailored response that identifies the animal and provides insightful
            information about their breed, characteristics, and care.
        </p>

        <div class="container">
            <div v-if="selectedImage" class="image-container">
                <img style="max-height:300px" :src="selectedImage" alt="Selected Image" />
            </div>
            <input class="form-control form-control-sm" v-if="prediction === null" type="file" ref="fileInput" @change="handleFileUpload" accept="image/*" />
            <button v-if="prediction !== null" class="btn btn-success" @click="handleCancel">Reset</button>

            <div v-if="prediction !== null" class="mt-2 mb-4">
                <p>Image of {{ prediction }}<br/>Here are some characteristics of {{ prediction }}.</p>
                <p><i>{{ fun_fact }}</i></p>

                <div v-if="!didGiveFeedBack" class="card p-4">
                    <form @submit="submitForm">
                        <div class="form-group">
                            <label for="predictionCorrect">Are you happy with the response you got?</label>

                            <select class="form-select" id="predictionCorrect" v-model="predictionCorrect">
                                <option value="yes" selected>Yes</option>
                                <option value="no">No</option>
                            </select>

                            <div v-if="predictionCorrect === 'no'" class="mt-2">
                                <label for="trueLabel">We are sorry to hear that. Can you provide us with the correct animal?</label>
                                <select class="form-select" id="trueLabel" v-model="trueLabel" required>
                                    <option value="Golden retriever">Golden retriever</option>
                                    <option value="German shepherd">German shepherd</option>
                                    <option value="French bulldog">French bulldog</option>
                                    <option value="Beagle">Beagle</option>
                                    <option value="Yorkshire Terrier">Yorkshire Terrier</option>
                                    <option value="Persian cat">Persian cat</option>
                                    <option value="Siamese cat">Siamese cat</option>
                                    <option value="Spyhnx cat">Spyhnx cat</option>
                                    <option value="Maine Coon">Maine Coon</option>
                                    <option value="Parrot">Parrot</option>
                                    <option value="Gold fish">Gold fish</option>
                                    <option value="Koi fish">Koi fish</option>
                                    <option value="other">Other</option>
                                </select>
                            </div>

                            <button class="mt-2 btn btn-success" type="submit">Submit</button>
                        </div>
                    </form>
                </div>
            </div>
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
            fun_fact: null,
            predictionCorrect: "yes",
            trueLabel: '',
            didGiveFeedBack: false
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

                this.submitToApi();
            }
        },

        submitToApi() {
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

            const formData = new FormData();
            formData.append("image", this.uploadedImage);

            //axios.post("http://localhost:5000/predict_online_model", formData)
            axios.post("http://localhost:5000/predict_local_model", formData)
                .then(response => {
                    this.prediction = response.data['label'];
                    this.predictionCorrect = "yes";
                    this.trueLabel = '';
                    this.didGiveFeedBack = false;
                    this.fun_fact = response.data['fun_fact'];

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
            formData.append("true_label", this.trueLabel || "");
            formData.append("description", "description_value");
            formData.append("time", new Date().toISOString());

            axios
                .post("http://localhost:5000/feedback", formData)
                .then((response) => {
                    console.log("Feedback submitted:", response.data);
                    this.didGiveFeedBack = true;
                })
                .catch((error) => {
                    console.log("Error submitting feedback:", error);
                });

        },

        handleCancel() {
            this.selectedImage = null;
            this.uploadedImage = null;
            this.prediction = null;
            this.predictionCorrect = "yes";
            this.trueLabel = '';
            this.didGiveFeedBack = false;
        },

        onCancel() {
            // nothing to do here
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
</style>