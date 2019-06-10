<template>
  <v-container grid-list-md>
    <h1>Articles</h1>

    <v-layout row wrap>
      <v-flex xs12 v-for="article in allArticles" :key="article.id">
        <v-card>
          <v-card-title primary-title>
            <h2 class="headline mb-0">{{ article.title }}</h2>
          </v-card-title>

          <div v-for="tag in article.tags" :key="tag">
            <v-chip @click="tagName(tag)">{{tag}}</v-chip>
          </div>

          <v-card-text>
            <vue-markdown>{{ article.overview }}</vue-markdown>
          </v-card-text>

          <v-card-actions>
            <v-btn color="orange">Edit</v-btn>
            <v-btn color="orange">Remove</v-btn>
          </v-card-actions>
        </v-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import { mapGetters, mapActions } from "vuex";
import VueMarkdown from "vue-markdown";
import axios from "axios";

export default {
  name: "Articles",
  components: { VueMarkdown },
  methods: {
    ...mapActions(["fetchArticles"]),

    async tagName(tagUrl) {
      const response = await axios.get(tagUrl);
      console.log(response.data.title);
    }
  },

  computed: mapGetters(["allArticles"]),
  created() {
    this.fetchArticles();
  }
};
</script>
