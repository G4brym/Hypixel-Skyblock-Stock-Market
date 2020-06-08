import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    version: null
  },
  mutations: {
    loadVersion(state, version) {
      state.version = version;
    }
  },
  actions: {},
  modules: {}
});
