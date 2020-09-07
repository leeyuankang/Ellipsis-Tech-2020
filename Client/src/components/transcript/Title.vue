<template>
    <b-container class='container'>
        <b-row class='word-container' align-v="center">
            <div class='general-container'>
                <div class='transcript-title'>{{labels.title}}</div>
                <div class='transcript-description'>{{labels.desc}}</div>
            </div>
        </b-row>
    </b-container>
</template>

<script>

export default {
  name: 'Header',
  data() {
      return {
          labels: {
              title:'Baidu, Inc. (BIDU) Q2 2020 Earnings Call Transcript',
              desc:'BIDU earnings call for the period ending June 30, 2020.'}
      }
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

.general-container{
    padding: 20px 20px 5px 20px;
    text-align: left;
    padding-bottom: 20px;
    width: 100%;
}

.transcript-title{
    font-size: 30px;
    font-weight: 600;
}

</style>
