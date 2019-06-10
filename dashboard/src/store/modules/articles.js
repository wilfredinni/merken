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

  // async fetchTags({ commit, url }) {
  //   const response = await axios.get(url);
  //   commit("setArticleTag", response.data.title)
  // }
};

const mutations = {
  setArticles: (state, articles) => (state.articles = articles),

  // setArticleTag() {
  //   for (let article in state.articles) {
  //     for (let tag in article.tags) {
  //       state.articles.article.tags
  //     }
  // }
};

export default {
  state,
  getters,
  actions,
  mutations
};
