import Vue from "vue";
import VueRouter from "vue-router";

import IndexView from "@views/IndexView";
import AboutView from "@views/AboutView";

Vue.use(VueRouter);

const routes = [
  {
    path: "",
    name: "index-view",
    component: IndexView
  },
  {
    path: "/about",
    name: "about-view",
    component: AboutView
  }
];

const router = new VueRouter({
  // mode: "history",
  base: process.env.BASE_URL,
  routes
});

export default router;
