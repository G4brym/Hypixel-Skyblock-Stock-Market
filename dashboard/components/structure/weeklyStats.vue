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
                <tr>
                  <td>Smith Drake</td>
                  <td>$12.546,45</td>
                  <td>18%</td>
                </tr>
                <tr>
                  <td>Vanessa Angel</td>
                  <td>$45.656,12</td>
                  <td>20%</td>
                </tr>
                <tr>
                  <td>Bacon Francis</td>
                  <td>$89.564,53</td>
                  <td>12.5%</td>
                </tr>
                <tr>
                  <td>Albom Mitch</td>
                  <td>$65.456,45</td>
                  <td>16%</td>
                </tr>
                <tr>
                  <td>Fenish Paul</td>
                  <td>$78.565,56</td>
                  <td>6%</td>
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
                <tr>
                  <td>Smith Drake</td>
                  <td>$12.546,45</td>
                  <td>18%</td>
                </tr>
                <tr>
                  <td>Vanessa Angel</td>
                  <td>$45.656,12</td>
                  <td>20%</td>
                </tr>
                <tr>
                  <td>Bacon Francis</td>
                  <td>$89.564,53</td>
                  <td>12.5%</td>
                </tr>
                <tr>
                  <td>Albom Mitch</td>
                  <td>$65.456,45</td>
                  <td>16%</td>
                </tr>
                <tr>
                  <td>Fenish Paul</td>
                  <td>$78.565,56</td>
                  <td>6%</td>
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
      selectedProduct: null
    };
  },
  methods: {
    selectProduct: function(value) {
      this.$store.commit("updateSelectedProduct", value);
      this.selectedProduct = null;
    }
  }
};
</script>
