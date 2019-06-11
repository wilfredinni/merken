import axios from "axios";

const state = {
  articles: []
};

const getters = {
  allArticles: state => state.articles
};

const actions = {
  async fetchArticles({ commit }) {
    const response = await axios.get("/api/articles/");
    commit("setArticles", response.data);
  },
};

const mutations = {
  setArticles: (state, articles) => (state.articles = articles),
};

export default {
  state,
  getters,
  actions,
  mutations
};
