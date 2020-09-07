<template>
  <div class='chart-container'>
    <section class="charts">
          <h3>Recommend Investment Portfolio</h3>
          <vue-highcharts :options="pieOptions" ref="pieChart"></vue-highcharts>
      </section>
  </div>
</template>
<script>
import VueHighcharts from "vue2-highcharts";
import * as data from "../assets/data.js";

export default {
  components: {
    VueHighcharts
  },
  data() {
    return {
      pieOptions: data.PieData
    };
  },
  mounted() {},
  methods: {}
};
</script>

<style scoped>
  .chart-container{
    margin-top: 100px;
  }
</style>