<template>
    <b-container class='container'>
        <b-row class='header-container'>
            <div>
                Earning Transcripts
            </div>
        </b-row>
        <b-row align-v="center" >
            <div v-for="transcript in transcripts" v-bind:key="transcript.title" class='transcript-container'>
                <router-link :to="transcript.url" class='transcript-title'>
                {{transcript.title}}
                </router-link>
                <div class='transcript-description'>
                {{transcript.desc}}
                </div>
            </div>
            
        </b-row>
    </b-container>
</template>

<script>

export default {
  name: 'Header',
  data() {
      return {
          transcripts: [
              {title:'Baidu, Inc. (BIDU) Q2 2020 Earnings Call Transcript', 
              desc:'BIDU earnings call for the period ending June 30, 2020.',
              url: '/transcript'},
              {title:'Baidu, Inc. (BIDU) Q1 2020 Earnings Call Transcript',
              desc:'BIDU earnings call for the period ending March 31, 2020.',
              url: '#'},
              {title:'Baidu, Inc. (BIDU) Q4 2019 Earnings Call Transcript',
              desc:'BIDU earnings call for the period ending December 31, 2019.',
              url:'#'}
              ]
      }
  },
 
}
</script>

<style scoped>

.container{
    padding-bottom: 20px;
    border-width: 0 0 1px 0;
    border-style: solid;
}

.header-container{
    padding: 20px 20px 5px 20px;
    font-size: 30px;
    font-weight: 600;
}

.transcript-container{
    padding: 20px 20px 5px 20px;
    text-align: left;
    padding-bottom: 20px;
    border-width: 1px 0 0 0;
    border-style: solid;
    width: 100%;
}

.transcript-title{
    font-size: 30px;
    font-weight: 600;
}

</style>
