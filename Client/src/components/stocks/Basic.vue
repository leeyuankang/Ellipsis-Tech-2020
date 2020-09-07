<template>
    <b-container class='container basic-container'>
        <b-row class='header'>
            <span>Basic Guide</span>
        </b-row>
         <b-card-group deck>
            <b-card v-for="card in cards" v-bind:key="card.id" img-alt="Image" img-top>
                <b-card-img :src="card.image" class='card-image'></b-card-img>
                <b-card-title class='title'>{{card.title}}</b-card-title>
                <b-card-text class='text'>{{card.text}}</b-card-text>
            </b-card>
         </b-card-group>
    </b-container>
</template>

<script>
export default {
  name: 'Basic',
  data() {
      return {
          cards : [
              {
                  id: 'research',
                  title: 'Research',
                  image: require('../../assets/research.jpeg'),
                  text: 'Research on companies starting from annual reports, earning transcripts and news.'
                },
              {
                  id: 'purchase',
                  title: 'Purchase',
                  image: require('../../assets/purchase.jpg'),
                  text: 'Order types are ways for you to purchase stocks! So plan wisely to decide which order type to use.'
                },
              {
                  id: 'optimize',
                  title: 'Optimize',
                  image: require('../../assets/optimize.png'),
                  text: "We're talking about long term success, so constantly tune your trading strategies to make sure you keep winning."
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
    border-width: 1px 0 1px 0;
    border-style: solid;
}

.header{
    padding: 20px;
    font-size: 30px;
    font-weight: 600;
}

.title{
    font-size: 24px;
    font-weight: 600;
}

.text{
    font-size: 18px;
    text-align: justify;
}

.card-image{
    height: 150px;
}

</style>
