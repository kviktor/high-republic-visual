import { createRouter, createWebHistory } from 'vue-router';

import EntityList from './components/EntityList.vue';

const router = createRouter({
  base: process.env.BASE_URL,
  history: createWebHistory(process.env.BASE_URL),
  routes: [
    { path: '/:ids*', name: "list", component: EntityList},
  ]
});

router.beforeEach((to) => {
  document.title = to.meta.title || "High Republic Visual Guide";
});

export default router;
