import { createApp } from 'vue'
import App from './App.vue'
import { LoadingPlugin } from 'vue-loading-overlay'
import 'vue-loading-overlay/dist/css/index.css'

const app = createApp(App)
app.use(LoadingPlugin)
app.mount('#app')
