<template>
    <b-container class='container basic-container'>
        <b-row class='header'>
            <span>Useful Videos</span>
        </b-row>
         <b-card-group deck>
             <b-card class='card' v-for="card in cards" v-bind:key="card.id">
                <b-embed
                type="iframe"
                aspect="16by9"
                :src= card.image
                allowfullscreen
                ></b-embed>
            </b-card>
         </b-card-group>
    </b-container>
</template>

<script>
export default {
  name: 'Video',
  data() {
      return {
          cards : [
              {
                  id: 'research-vid',
                  title: 'Research',
                  image: "https://www.youtube.com/embed/seN4gz_B1Uo"
                },
              {
                  id: 'purchase-vid',
                  title: 'Purchase',
                  image: "https://www.youtube.com/embed/DF23jO8Y0n0"
                },
              {
                  id: 'optimize-vid',
                  title: 'Optimize',
                  image: "https://www.youtube.com/embed/YtrMGKLRtwA"
                }
          ]
      }
  }
}
</script>

<style scoped>
.basic-container{
    margin-top: 20px;
    padding-bottom: 20px;
    border-width: 0 0 1px 0;
    border-style: solid;
}

.header{
    padding: 20px;
    font-size: 30px;
    font-weight: 600;
}

.card-body{
    padding: 0;
}

</style>
