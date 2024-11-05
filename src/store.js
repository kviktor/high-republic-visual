import { createStore } from 'vuex';
import structure from './assets/structure.json';

const store = createStore({
    state() {
        return {
            "entities": structure,
        }
    },
    getters: {
        getEntities(state) {
            return state.entities;
        },
        getEntityById: (state) => (parent, id) => {
            return state.entities.find(entity => entity.slug === id && entity.parent === parent);
        }
    }
});

export default store;