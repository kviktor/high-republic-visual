import { createStore } from 'vuex';
import structure from './assets/structure.json';

const store = createStore({
    state() {
        return {
            "entities": structure,
            "currentEntities": [],
        }
    },
    getters: {
        getEntities(state) {
            return state.entities;
        },
        getEntityById: (state) => (id) => {
            return state.entities.find(entity => entity.id === id);
        },
        getEntityBySlug: (state) => (slug, parent) => {
            return state.entities.find(entity => entity.slug === slug && entity.parent === parent);
        },
        getCurrentEntities(state) {
            return state.currentEntities;
        },
        getParentEntitiesById: (state, getters) => (id) => {
            var parentEntities = [];
            var entity = getters.getEntityById(id);

            if (entity.parent) {
                var parent = entity.parent;
                while(parent !== null) {
                    entity = getters.getEntityById(parent);
                    parentEntities.push(entity);
                    parent = entity.parent;
                }
            }

            return parentEntities.reverse();
        }
    },
    mutations: {
        setCurrentEntities(state, entities) {
            state.currentEntities = entities;
        }
    },
    actions: {
        setCurrentEntities(context, entities) {
            context.commit('setCurrentEntities', entities);
        }
    }
});

export default store;