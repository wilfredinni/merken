<template>
  <v-layout row class="mb-3" wrap>

    <!-- all articles -->
    <v-tooltip top>
      <template v-slot:activator="{ on }">
        <v-btn @click="filterArticles('all')" icon v-on="on">
          <v-icon color="primary">dashboard</v-icon>
        </v-btn>
      </template>
      <span>All Articles</span>
    </v-tooltip>

    <!-- published -->
    <v-tooltip top>
      <template v-slot:activator="{ on }">
        <v-btn @click="filterArticles('published')" icon v-on="on" class="icon-published">
          <v-icon>check_circle</v-icon>
        </v-btn>
      </template>
      <span>Published</span>
    </v-tooltip>

    <!-- featured -->
    <v-tooltip top>
      <template v-slot:activator="{ on }">
        <v-btn @click="filterArticles('featured')" icon v-on="on" class="icon-featured">
          <v-icon>stars</v-icon>
        </v-btn>
      </template>
      <span>Featured</span>
    </v-tooltip>

    <!-- draft -->
    <v-tooltip top>
      <template v-slot:activator="{ on }">
        <v-btn @click="filterArticles('draft')" icon v-on="on" class="icon-draft">
          <v-icon>work</v-icon>
        </v-btn>
      </template>
      <span>Draft</span>
    </v-tooltip>

    <!-- unpublished -->
    <v-tooltip top>
      <template v-slot:activator="{ on }">
        <!-- TODO: code this filter -->
        <v-btn icon v-on="on" class="icon-unpublished">
          <v-icon>watch_later</v-icon>
        </v-btn>
      </template>
      <span>Unpublished</span>
    </v-tooltip>

    <v-spacer></v-spacer>

    <v-tooltip top>
      <template v-slot:activator="{ on }">
        <v-btn icon v-on="on">
          <v-icon color="primary">add_circle</v-icon>
        </v-btn>
      </template>
      <span>New Article</span>
    </v-tooltip>

  </v-layout>
</template>

<script>
import { mapActions } from "vuex";

export default {
  name: "FilterArticle",

  methods: {
    ...mapActions(["filterArticles"]),
  },
};
</script>

<style scoped>
.icon-published {
  color: #3cd1c2;
}
.icon-draft {
  color: #ffaa2c;
}
.icon-featured {
  color: #9652ff;
}
.icon-unpublished {
  color: #f83e70;
}
</style>
