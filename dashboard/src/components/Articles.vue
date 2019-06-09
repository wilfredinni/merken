<template>
  <v-container fluid grid-list-md>
    <h1>Articles</h1>

    <v-layout row wrap>
      <v-flex sm6 xs12 v-for="article in allArticles" :key="article.id">
        <v-card>
          <v-card-title primary-title>
            <h3 class="headline mb-0">{{ article.title }}</h3>
          </v-card-title>

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

export default {
  name: "Articles",
  components: { VueMarkdown },
  methods: { ...mapActions(["fetchArticles"]) },
  computed: mapGetters(["allArticles"]),
  created() {
    this.fetchArticles();
  }
};
</script>
