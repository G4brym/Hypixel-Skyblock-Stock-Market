<template>
  <div class="row mb-4">
    <div class="col-md-6">
      <div class="card card-statistics h-100">
        <div class="card-header">
          <h4 class="card-title">Weekly Top Gainers</h4>
        </div>
        <div class="card-body p-0">
          <div class="table-responsive">
            <table class="table table-borderless mb-0">
              <thead class="bg-light">
                <tr>
                  <th scope="col">Stock</th>
                  <th scope="col">Current Price</th>
                  <th scope="col">% change</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="product in gainers" :key="product.id" @click="$store.commit('updateSelectedProduct', product.id)">
                  <td v-text="product.name"></td>
                  <td v-text="product.current_value"></td>
                  <td>{{ product.change }}%</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
    <div class="col-md-6">
      <div class="card card-statistics h-100">
        <div class="card-header">
          <h4 class="card-title">Weekly Top Losers</h4>
        </div>
        <div class="card-body p-0">
          <div class="table-responsive">
            <table class="table table-borderless mb-0">
              <thead class="bg-light">
                <tr>
                  <th scope="col">Stock</th>
                  <th scope="col">Current Price</th>
                  <th scope="col">% change</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="product in losers" :key="product.id" @click="$store.commit('updateSelectedProduct', product.id)">
                  <td v-text="product.name"></td>
                  <td v-text="product.current_value"></td>
                  <td>{{ product.change }}%</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      gainers: [],
      losers: []
    };
  },
  methods: {
    loadData: function() {
      this.$http.get("/market/weekly/").then(response => {
        this.gainers = response.data.gainers;
        this.losers = response.data.losers;
      });
    }
  },
  mounted: function() {
    this.loadData();
  }
};
</script>

<style scoped>
tbody tr:hover {
  cursor: pointer;
  background-color: #222222;
}
</style>
