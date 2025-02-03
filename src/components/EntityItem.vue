<template>
    <div class="col">
        <div v-if="is_image" class="card h-100">
            <img :src="thumbnail_src" class="card-img-top" alt="...">
            <div class="card-body">
                <p class="card-text">{{ name }}</p>
                <a :href="image_src" class="btn btn-primary stretched-link" target="_blank">View</a>
            </div>
        </div>
        <div v-else class="card h-100">
            <div class="card-body">
                <h5 class="card-title">{{ get_name }}</h5>
            </div>
            <div class="card-footer text-end">
                <router-link :to="link" class="btn btn-primary stretched-link">View</router-link>
            </div>
        </div>
    </div>
</template>

<script>


export default {
    props: ["id", "name", "slug"],
    computed: {
        is_image() {
            return this.name.indexOf(".") !== -1;
        },
        get_name() { 
            if (this.$route.name === "list") {
                return this.name;
            } else {
                return this.$store.getters.getParentEntitiesById(this.id).map(entity => entity.name).concat(this.name).join(" / ");
            }
        },
        thumbnail_src() {
            return this.image_src.replace("/images/", "/thumbnails/");
        },
        image_src() {
            var arr = [];

            this.$store.getters.getParentEntitiesById(this.id).forEach(entity => {
                arr.push(entity.name);
            });

            arr.unshift("images");
            arr.push(this.name);

            return process.env.BASE_URL + arr.join('/');
        },
        link() {
            var parents = this.$store.getters.getParentEntitiesById(this.id).map(entity => entity.slug);

            return {
                name: "list",
                params: {
                    ids: parents.concat(this.slug),
                },
            }
        }
    }
}
</script>

<style scoped>
    .card-img-top {
        height: 300px;
        object-fit: cover;
    }
</style>