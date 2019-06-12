import axios from "axios";

const state = {
  articles: [],
  tags: []
};

const getters = {
  allArticles: state => state.articles,
  allTags: state => state.tags
};

const actions = {
  async fetchArticles({ commit }) {
    const response = await axios.get("/api/articles/");
    commit("setArticles", response.data);
  },

  async fetchTags({ commit }) {
    const response = await axios.get("/api/tags/");
    commit("setTags", response.data);
  },
};

const mutations = {
  setArticles: (state, articles) => (state.articles = articles),
  setTags: (state, tags) => (state.tags = tags),
};

export default {
  state,
  getters,
  actions,
  mutations
};
