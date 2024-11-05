import { createRouter, createWebHistory } from 'vue-router';

import EntityList from './components/EntityList.vue';

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/:ids*', name: "list", component: EntityList},
  ]
});

export default router;