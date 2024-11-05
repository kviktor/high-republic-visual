import { createApp } from 'vue'

import router from './router.js';
import store from './store.js';
import App from './App.vue';

import './styles.scss'


const app = createApp(App)

app.use(router);
app.use(store);
app.mount('#app')
