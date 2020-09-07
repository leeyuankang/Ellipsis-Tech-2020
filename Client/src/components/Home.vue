<template>
  <div id="home">
    <Label />
    <Basic />
    <Video />
    <Company />
  </div>
</template>

<script>
import Label from './stocks/Label.vue'
import Basic from './stocks/Basic.vue'
import Video from './stocks/Video.vue'
import Company from './stocks/Company.vue'

export default {
  name: 'Home',
  components: {
    Label,
    Basic,
    Video,
    Company
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  /* margin-top: 60px; */
}
</style>
