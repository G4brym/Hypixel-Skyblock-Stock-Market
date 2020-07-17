<template>
  <div>
    <h1 class="mb-3 text-center">Hypixel Skyblock Stock Market</h1>
    <div class="row mb-4">
      <div class="col-md-12 chart-holder">
        <highcharts :constructorType="'stockChart'" class="hc" :options="chartOptions" ref="highchart" />
      </div>
    </div>
    <weekly-stats />
  </div>
</template>

<script>
// import LoadingAnimation from "@components/structure/loading";
import WeeklyStats from "@components/structure/weeklyStats";

export default {
  data() {
    return {
      chartOptions: {
        title: {
          text: "Stock price"
        },
        yAxis: {
          min: 0
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
              type: "month",
              count: 1,
              text: "1M"
            },
            {
              type: "all",
              count: 1,
              text: "All"
            }
          ],
          selected: 2,
          inputEnabled: false
        },
        series: [
          {
            type: "candlestick",
            data: [],
            tooltip: {
              valueDecimals: 2
            }
          }
        ]
      }
    };
  },
  methods: {
    loadChart: function() {
      this.$http.get(`/market/${this.$store.state.selectedProduct}/prices/`).then(response => {
        this.$refs.highchart.chart.setTitle({ text: `${response.data.product.name} Stock price` });
        this.$refs.highchart.chart.series[0].name = response.data.product.name;
        this.$refs.highchart.chart.series[0].setData(response.data.data, true);
      });
    }
  },
  watch: {
    "$store.state.selectedProduct": function() {
      this.loadChart();
    }
  },
  mounted: function() {
    this.loadChart();
  },
  components: {
    WeeklyStats
    // LoadingAnimation
  }
};
</script>
