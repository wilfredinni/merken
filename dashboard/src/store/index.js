import Vue from "vue";
import Vuex from "vuex";
import articles from "./modules/articles";
import newArticle from "./modules/newArticle";

// load vuex
Vue.use(Vuex);

// create store
export default new Vuex.Store({
  modules: {
    articles,
    newArticle,
  }
});
