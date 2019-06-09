import Vue from "vue";
import Vuex from "vuex";
import articles from "./modules/articles";

// load vuex
Vue.use(Vuex);

// create store
export default new Vuex.Store({
  modules: {
    articles
  }
});
