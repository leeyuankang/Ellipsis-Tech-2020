<template>
  <div id="transcript">
      <Header />
      <Title />
      <Content />
  </div>
</template>

<script>

import Header from './profile/Header.vue'
import Title from './transcript/Title.vue'
import Content from './transcript/Content.vue'

export default {
  name: 'Transcript',
  components: {
      Header,
      Content,
      Title
  }
}
</script>
