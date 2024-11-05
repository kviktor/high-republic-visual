<template>
  <main>
    <div class="container py-4">
      <the-header></the-header>
      <router-view></router-view>
      <the-jumbotron v-show="!$route.params.ids"></the-jumbotron>
    </div>
  </main>
</template>

<script>
import TheHeader from './components/TheHeader.vue'
import TheJumbotron from './components/TheJumbotron.vue'

export default {
  name: 'App',
  components: {
    TheHeader,
    TheJumbotron,
  }
}
</script>
