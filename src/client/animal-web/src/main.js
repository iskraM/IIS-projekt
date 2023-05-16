import App from './App.vue'
import { createApp } from 'vue'
import { LoadingPlugin } from 'vue-loading-overlay'

import 'vue-loading-overlay/dist/css/index.css'

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'


const app = createApp(App)
app.use(LoadingPlugin)
app.mount('#app')
