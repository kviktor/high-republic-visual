<template>
    <div class="row row-cols-1 row-cols-sm-2 row-cols-md-3 row-cols-lg-4 g-4">
        <entity-item
            v-for="entity in entities"
            :key="entity.id"
            :id="entity.id"
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

            if (this.$route.name === "list") {
                var currentEntities = this.$store.getters.getCurrentEntities;
                var parent = null;
                if(currentEntities.length > 0) {
                    parent = currentEntities.at(-1).id;
                }
                
                return entities.filter((entity) => entity.parent === parent);
            } else {
                return entities.filter((entity) => entity.name.toLowerCase().includes(this.$route.params.searchQuery.toLowerCase())).sort((a, b) => a.name.indexOf(".") < b.name.indexOf(".") ? -1 : 1);
            }

        },
    }
};
</script>

<style scoped>
span span {
    padding: 10px;
}
</style>