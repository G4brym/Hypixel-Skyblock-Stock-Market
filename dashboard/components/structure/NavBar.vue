<template>
  <nav class="navbar navbar-expand-lg navbar-dark bg-dark mb-4">
    <div class="container">
      <router-link :to="{ name: 'index-view' }" class="navbar-brand" href="">Hystocks.com</router-link>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarColor02" aria-controls="navbarColor02" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>

      <div class="collapse navbar-collapse">
        <ul class="navbar-nav mr-auto">
          <li class="nav-item">
            <router-link :to="{ name: 'about-view' }" class="nav-link" href="">About</router-link>
          </li>
        </ul>
        <form class="form-inline ml-auto my-2 my-lg-0">
          <v-select
            style="width: 250px"
            class="style-chooser"
            placeholder="Search for Potatoes, Carrots, ..."
            :value="selectedProduct"
            label="name"
            :options="Object.values($store.state.products)"
            :reduce="obj => obj.id"
            @input="selectProduct"
          ></v-select>
        </form>
      </div>
    </div>
  </nav>
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

      if (this.$route.name !== "index-view") {
        this.$nextTick(() => {
          this.$router.push({ name: "index-view" });
        });
      }
    }
  }
};
</script>
