<template>
    <div class='container trading-vue-container'>
        <trading-vue height=400 width=1100 :data="this.$data"></trading-vue>
    </div>
</template>
<script>

import TradingVue from 'trading-vue-js'
import axios from 'axios'

export default {
    name: 'app',
    components: { TradingVue },
    data() {
        return {
            ohlcv: null
        }
    },
    mounted() {
        axios
            .get('http://54.179.2.124:8000/history')
            .then(response => {
                // console.log(response.data)

                var output = []

                for(var dates in response.data){
                    var values = response.data[dates]
                    // console.log(values.Timestamp)
                    var data = [values.Timestamp, values.Open, values.High, values.Low, values.Close, values.Volume]
                    output.push(data)
                }
                // console.log(output)
                this.ohlcv = output
            })
  }
}

</script>

<style>
.trading-vue-container{
    margin-top: 20px;
    width: 100%;
    padding-bottom: 20px;
    border-width: 0 0 1px 0;
    border-style: solid;
}
</style>