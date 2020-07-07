import Vue from "vue";
import router from "./router";
import store from "./store";
import Highcharts from "highcharts";
import HighchartsVue from "highcharts-vue";
import stockInit from "highcharts/modules/stock";
stockInit(Highcharts);
import BootstrapVue from "bootstrap-vue";
Vue.use(BootstrapVue);

// This imports all the layout components such as <b-container>, <b-row>, <b-col>:
import { LayoutPlugin } from "bootstrap-vue";
Vue.use(LayoutPlugin);

// This imports <b-modal> as well as the v-b-modal directive as a plugin:
import { ModalPlugin } from "bootstrap-vue";
Vue.use(ModalPlugin);

// This imports <b-card> along with all the <b-card-*> sub-components as a plugin:
import { CardPlugin } from "bootstrap-vue";
Vue.use(CardPlugin);

// This imports directive v-b-scrollspy as a plugin:
import { VBScrollspyPlugin } from "bootstrap-vue";
Vue.use(VBScrollspyPlugin);

// This imports the dropdown and table plugins
import { DropdownPlugin, TablePlugin } from "bootstrap-vue";
Vue.use(DropdownPlugin);
Vue.use(TablePlugin);

import axios from "axios";
import "./scss/entry.scss";

import NavBar from "@components/structure/NavBar";

//////////
// Load font awesome
//////////
import { library } from "@fortawesome/fontawesome-svg-core";
import { fas } from "@fortawesome/free-solid-svg-icons";
import { far } from "@fortawesome/free-regular-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";

library.add(fas);
library.add(far);
Vue.component("fa", FontAwesomeIcon);
Vue.use(HighchartsVue);

//////////
// Load api url from django
//////////
// eslint-disable-next-line
let apiUrl = document.head.querySelector("meta[name=\"url\"]").content;

axios.defaults.baseURL = apiUrl;
Vue.prototype.$http = axios;

//////////
// Load git version from django
//////////
try {
  // eslint-disable-next-line
  let version = JSON.parse(document.head.querySelector("meta[name=\"version\"]").content);

  store.commit("loadVersion", version);
} catch (err) {
  // eslint-disable-next-line no-console
  console.log("Error loading version");
}

Vue.config.productionTip = false;

new Vue({
  router,
  store,
  components: {
    "nav-bar": NavBar
  }
}).$mount("#app");
