import { createRouter, createWebHistory } from 'vue-router';

import store from './store.js';

import EntityList from './components/EntityList.vue';

const router = createRouter({
  base: process.env.BASE_URL,
  history: createWebHistory(process.env.BASE_URL),
  routes: [
    { path: '/search/:searchQuery', name: "search", component: EntityList},
    { path: '/:ids*', name: "list", component: EntityList},
  ]
});


export default router;

router.beforeEach((to) => {
  var entities = [];
  var parent = null;

  var ids = to.params.ids || [];
  ids.forEach(part => {
    var entity = store.getters.getEntityBySlug(part, parent);
    parent = entity.id;
    entities.push(entity);
  });
  store.dispatch('setCurrentEntities', entities);

  document.title = to.meta.title || "High Republic Visual Guide";
});