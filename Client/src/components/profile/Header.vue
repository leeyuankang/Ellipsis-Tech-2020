<template>
    <b-container class='container'>
        <b-row class='word-container' align-v="center">
            <div class='general-container'>
                <div class='ticker-label'>{{labels[0].stock}}</div>
                <div class='company-label'>{{labels[0].company}}</div>
            </div>
            <div class='logo-container'>
                <img class='logo' src="../../assets/baidu.png">
            </div>
        </b-row>
        <b-row>
            <div class='price-container'>
                <div class='price'>{{price}}USD</div>
                <div :class="{rise: change > 0, fall: change <0}">
                    <span>{{change}}</span>
                </div>
            </div>
        </b-row>
    </b-container>
</template>

<script>

import axios from 'axios'

export default {
  name: 'Header',
  data() {
      return {
          labels: [{stock:'BIDU:US', company:'Baidu Inc'}],
          price: null,
          change: null
      }
  },
  mounted() {
        axios
            .get('http://54.179.2.124:8000/price')
            .then(response => {
                // console.log(response.data)

                var ticker = response.data['BIDU']

                this.price = ticker[0]
                this.change = ticker[1]
            })
  }
}
</script>

<style scoped>

.container{
    padding-bottom: 20px;
    border-width: 0 0 1px 0;
    border-style: solid;
}

.word-container{
    height: 100%;
    
}

.general-container, .price-container{
    padding: 20px 20px 5px 20px;
    font-size: 22px;
    font-weight: 600;
}

.price-container{
    display:flex;
}

.logo-container{
    margin-left: auto;
}

.logo{
    width: 150px;
    height: 75px;
}

.ticker-label, .company-label{
    text-align: left;
}

.price{
    margin-right: 20px;
    font-size: 40px;
}

.fall{
    color: rgb(238, 37, 37);
    position: relative;
}

.rise{
    color: rgb(0, 255, 0);
    position: relative;
}

.fall span, .rise span{
    bottom: 10px;
    position: absolute;
}
</style>
