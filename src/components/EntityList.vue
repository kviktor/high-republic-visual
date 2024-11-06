<template>
    <div class="row row-cols-1 row-cols-sm-2 row-cols-md-3 row-cols-lg-4 g-4">
        <entity-item
            v-for="entity in entities"
            :key="entity.parent + '_' + entity.slug"
            :slug="entity.slug"
            :name="entity.name"
        ></entity-item>
    </div>
</template>

<script>
import EntityItem from './EntityItem.vue';

export default {
    components: {
        EntityItem,
    },
    computed: {
        entities() {
            var entities = this.$store.getters.getEntities;

            var parent = null;
            if (this.$route.params.ids) {
                parent = this.$route.params.ids.join("_");
            }

            return entities.filter((entity) => entity.parent === parent);
        },
    }
};
</script>

<style scoped>
span span {
    padding: 10px;
}
</style>