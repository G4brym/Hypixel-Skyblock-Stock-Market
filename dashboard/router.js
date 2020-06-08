import Vue from "vue";
import VueRouter from "vue-router";

import IndexView from "@views/IndexView";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "index-view",
    component: IndexView
  }
];

const router = new VueRouter({
  // mode: "history",
  base: process.env.BASE_URL,
  routes
});

export default router;
