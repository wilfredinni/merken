import axios from "axios";

const apiUrls = {
  articles: "/api/articles/"
};

const state = {
  articles: [],
  articlesCopy: [],
  tags: []
};

const getters = {
  allArticles: state => state.articles,
  allTags: state => state.tags
};

const actions = {
  async fetchArticles({ commit }) {
    const response = await axios.get(apiUrls.articles);
    commit("setArticles", response.data);
  },

  filterArticles({ commit }, status) {
    if (status === "published") {
      commit("filterPublished", status);
    } else if (status === "featured") {
      commit("filterFeatured", status);
    } else if (status === "draft") {
      commit("filterDraft", status);
    } else if (status === "all") {
      commit("filterAll", status);
    }
  },

  async fetchTags({ commit }) {
    const response = await axios.get("/api/tags/");
    commit("setTags", response.data);
  }
};

const mutations = {
  setArticles(state, articles) {
    state.articles = articles;
    state.articlesCopy = articles;
  },

  setTags: (state, tags) => (state.tags = tags),

  filterAll: state => (state.articles = state.articlesCopy),

  filterPublished(state) {
    state.articles = state.articlesCopy;
    state.articles = state.articles.filter(
      article => article.is_draft === false
    );
  },

  filterFeatured(state) {
    state.articles = state.articlesCopy;
    state.articles = state.articles.filter(
      article => article.is_featured === true
    );
  },

  filterDraft(state) {
    state.articles = state.articlesCopy;
    state.articles = state.articles.filter(
      article => article.is_draft === true
    );
  }
};

export default {
  state,
  getters,
  actions,
  mutations
};
