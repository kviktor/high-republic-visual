import { createRouter, createWebHistory } from 'vue-router';

import EntityList from './components/EntityList.vue';

const router = createRouter({
  base: process.env.BASE_URL,
  history: createWebHistory(process.env.BASE_URL),
  routes: [
    { path: '/:ids*', name: "list", component: EntityList},
  ]
});

export default router;
