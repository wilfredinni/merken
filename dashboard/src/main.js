import "@babel/polyfill";
import Vue from "vue";
import "./plugins/vuetify";
import "./plugins/vuetify";
import "material-design-icons-iconfont/dist/material-design-icons.css";
import Vuetify from "vuetify";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import moment from "moment";

Vue.filter("formatDate", function(value) {
  if (value) {
    return moment(String(value)).format("MMM DD YYYY");
  }
});

Vue.use(Vuetify, {
  iconfont: "md"
});

Vue.config.productionTip = false;

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount("#app");
