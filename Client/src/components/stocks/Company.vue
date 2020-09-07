<template>
    <b-container class='container basic-container'>
        <b-row class='header'>
            <span>Companies</span>
        </b-row>
        <b-row class='excerpt'>
            <span>Learn what to look out for when doing your company research with our auto-annotations</span>
        </b-row>
        <table class='table'>
            <tr>
                <td class='table-header'>Stock</td>
                <td class='table-header'>Company Name</td>
                <td class='table-header'>Price</td>
                <td class='table-header'>Change</td>
            </tr>
            <tr v-for="card in cards" v-bind:key="card.stock">
                <td><router-link :to="card.url">{{card.stock}}</router-link></td>
                <td>{{card.company}}</td>
                <td>{{card.price}}USD</td>
                <td :class="{rise: card.change > 0, fall: card.change <0}">{{card.change}}</td>
            </tr>
        </table>
    </b-container>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Company',
  data() {
      return {
          cards : [
              {stock:'BIDU', company: 'Baidu Inc', price: null, change: null, url:'/baidu'},
              {stock:'TSLA', company: 'Tesla Inc', price: null, change: null, url:'#'},
              {stock:'UBER', company:'Uber Technologies Inc', price:null, change:null, url:'#'}
          ],
      }
  },
   mounted() {
        axios
            .get('http://54.179.2.124:8000/price')
            .then(response => {
                console.log(response.data)
                console.log(this.cards)
                for(var index in this.cards){

                    var card = this.cards[index]

                    card.price = response.data[card.stock][0]
                    card.change = response.data[card.stock][1]
                }
            })
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
    padding: 20px 0 0 20px;
    font-size: 30px;
    font-weight: 600;
}

.table-header{
    font-weight: 600;
}

.excerpt{
    padding: 20px;
    font-size: 14px;
    text-align: left;
}

.card-body{
    padding: 0;
}

.fall{
    color: rgb(238, 37, 37);
}

.rise{
    color: rgb(0, 255, 0)
}

</style>
