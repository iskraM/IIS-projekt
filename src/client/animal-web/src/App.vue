<template>
  <AddPicture />
</template>

<!-- npm run serve -->

<script>
import AddPicture from './components/AddPicture.vue'

export default {
  name: 'App',
  components: {
    AddPicture,
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  padding-top: 30px;
  padding-bottom: 60px;
}
</style>
