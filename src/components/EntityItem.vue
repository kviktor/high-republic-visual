<template>
    <div class="col">
        <div v-if="is_image" class="card h-100">
            <img :src="src" class="card-img-top" alt="...">
            <div class="card-body">
                <p class="card-text">{{ name }}</p>
                <a :href="src" class="btn btn-primary stretched-link" target="_blank">View</a>
            </div>
        </div>
        <div v-else class="card h-100">
            <div class="card-body">
                <h5 class="card-title">{{ name }}</h5>
            </div>
            <div class="card-footer text-end">
                <router-link :to="link" class="btn btn-primary stretched-link">View</router-link>
            </div>
        </div>
    </div>
</template>

<script>


export default {
    props: ["name", "slug"],
    computed: {
        is_image() {
            return this.name.indexOf(".") !== -1;
        },
        src() {
            var arr = [];
            var parent = null;

            this.$route.params.ids.forEach(slug => {
                var entity = this.$store.getters.getEntityById(parent, slug);
                arr.push(entity.name);

                if(parent === null) {
                    parent = entity.slug;
                } else {
                    parent += "_" + entity.slug;
                }
            });

            arr.unshift("images");
            arr.push(this.name);

            return `${process.env.BASE_URL}${arr.join("/")}`;
        },
        link() {
            return {
                name: "list",
                params: {
                    ids: (this.$route.params.ids ? this.$route.params.ids.map(p => p) : []).concat(this.slug),
                },
            }
        }
    }
}
</script>

<style scoped>
    .card-img-top {
        height: 15vw;
        object-fit: cover;
    }
</style>