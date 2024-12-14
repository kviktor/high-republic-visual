<template>
    <header class="pb-3 mb-2">
        <div class="container">
            <router-link to="/" class="navbar-brand d-flex align-items-center">
                <img :src="logo_url" alt="High Republic Visual" class="me-4" height="50"/>
                <span style="font-size: 2.5rem;">The High Republic Visual Guide</span>
            </router-link>
        </div>
    </header>
    <nav>
        <ol class="breadcrumb p-3 bg-body-tertiary rounded-3">
            <li v-for="(crumb, index) in breadcrumbs" :key="crumb.name" :class="['breadcrumb-item', { active: index === breadcrumbs.length - 1 }]">
                <router-link v-if="index !== breadcrumbs.length - 1" :to="crumb.link" class="">{{ crumb.name }}</router-link>
                <span v-else>{{ crumb.name }}</span>
            </li>
        </ol>
    </nav>
</template>

<script>
export default {
    computed: {
        logo_url() {
            return process.env.BASE_URL + 'logo.webp';
        },
        breadcrumbs() {
            var breadcrumbs = []

            if (this.$route.params.ids) {
                var parent = [];
                this.$route.params.ids.forEach(part => {
                    var entity = this.$store.getters.getEntityById(parent.length > 0 ? parent.join("_") : null, part);
                    parent.push(entity.slug);

                    breadcrumbs.push({
                        name: entity.name,
                        link: {
                            name: "list",
                            params: {
                                ids: structuredClone(parent),
                            },
                        },
                    });
                });
            }

            breadcrumbs.unshift(
                {
                    "name": "Home",
                    "link": {
                        "name": "list",
                    }
                }
            )

            return breadcrumbs;
        }
    }
};
</script>

<style scoped>
nav {
    svg {
        width: 1rem;
        height: 1rem;
    }

}
</style>
