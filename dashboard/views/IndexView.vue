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
      selectedProduct: 208,
      loaded: false,
      chartOptions: {
        title: {
          text: "AAPL stock price by minute"
        },
        rangeSelector: {
          buttons: [
            {
              type: "day",
              count: 1,
              text: "1D"
            },
            {
              type: "day",
              count: 3,
              text: "3D"
            },
            {
              type: "day",
              count: 7,
              text: "1W"
            },
            {
              type: "all",
              count: 1,
              text: "All"
            }
          ],
          selected: 1,
          inputEnabled: false
        },

        series: null
      }
    };
  },
  mounted: function() {
    this.$http.get(`/market/${this.selectedProduct}/prices/`).then(response => {
      this.chartOptions.series = [
        {
          name: "AAPL",
          type: "candlestick",
          data: response.data,
          tooltip: {
            valueDecimals: 2
          }
        }
      ];
      this.loaded = true;
    });
  }
};
</script>
