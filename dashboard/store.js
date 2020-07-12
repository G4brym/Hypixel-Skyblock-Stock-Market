import Vue from "vue";
import Vuex from "vuex";
import axios from "axios";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    version: null,
    selectedProduct: 36,
    products: {}
  },
  mutations: {
    loadProducts(state, products) {
      products.forEach(function(product) {
        Vue.set(state.products, product.id, product);
      });
    },
    loadVersion(state, version) {
      state.version = version;
    },
    updateSelectedProduct(state, productId) {
      state.selectedProduct = productId;
    }
  },
  actions: {
    loadProducts({ commit }) {
      axios.get("/products/").then(response => {
        commit("loadProducts", response.data);
      });
    }
  },
  modules: {}
});
