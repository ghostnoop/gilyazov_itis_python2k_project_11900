import {createApp} from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import GAuth from 'vue3-google-oauth2'

const app = createApp(App)
const gAuthOptions = {
    clientId: '575955870064-rdut3du40mo6aateq4048e8nj86h28aj.apps.googleusercontent.com',
    scope: 'email openid profile',
    fetch_basic_profile: true
}
app.use(store).use(router).use(GAuth, gAuthOptions).mount('#app')
