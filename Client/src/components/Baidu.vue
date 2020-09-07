<template>
  <div id="baidu">
      <Header />
      <Graph />
      <TranscriptList />
  </div>
</template>

<script>

import Header from './profile/Header.vue'
import Graph from './profile/Graph.vue'
import TranscriptList from './profile/TranscriptList.vue'

export default {
  name: 'Baidu',
  components: {
      Header,
      Graph,
      TranscriptList
  }
}
</script>
