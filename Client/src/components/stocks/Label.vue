<template>
    <b-container class='image-container' v-bind:style="{ backgroundImage: 'url(' + stocksURL + ')' }">
        <b-row class='word-container' align-v="center">
            <div class='word'>
                <span>{{labels[0].title}}</span>
            </div>
        </b-row> 
    </b-container>
</template>

<script>
export default {
  name: 'Label',
  data() {
      return {
          labels: [{ id: 'default', title: 'Stocks'}]
      }
  },
  computed: {
     stocksURL() {
         return require('../../assets/stocks.jpg')
     }
   }

}
</script>

<style scoped>
.image-container{
    background-size: contain;
    max-width: 100%;
    height: 200px;
}

.word-container{
    height: 100%;
}

.word{
    position: relative;
    margin:auto;
    z-index: 1;
    font-size: 48px;
    font-weight: 600;
    color: white;
}
</style>
