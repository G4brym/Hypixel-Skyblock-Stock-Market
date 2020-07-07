<template>
  <div>
    <h1>WIP</h1>
    <template v-if="loaded">
      <highcharts :constructorType="'stockChart'" class="hc" :options="chartOptions" ref="chart"></highcharts>
    </template>
  </div>
</template>

<script>
export default {
  data() {
    return {
      loaded: false,
      chartOptions: {
        series: [
          {
            data: []
          }
        ]
      }
    };
  }
};
</script>
