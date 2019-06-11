<template>
  <div>
    <v-container my-2>

      <v-layout row class="mb-3" wrap>
        <v-btn icon>
          <v-icon color="primary">dashboard</v-icon>
        </v-btn>

        <v-btn icon>
          <v-icon color="success">check_circle</v-icon>
        </v-btn>

        <v-btn icon>
          <v-icon color="warning">work</v-icon>
        </v-btn>

        <v-btn icon>
          <v-icon color="error">watch_later</v-icon>
        </v-btn>

        <v-spacer></v-spacer>
        <v-btn icon>
          <v-icon color="primary">add_circle</v-icon>
        </v-btn>
      </v-layout>

      <v-card grid-list-xl v-for="article in allArticles" :key="article.id">
        <v-layout row wrap pa-2 :class="borderStatusCard(article)">
          <v-flex xs12 md6>
            <div class="mt-0 mb-1">{{ article.title }}</div>
            <div class="caption grey--text">#python #packaging</div>
          </v-flex>

          <v-flex xs5 sm6 md2>
            <div class="caption grey--text">Publish date</div>
            <div class="mt-0 mx-0 px-0">{{ article.created_at | formatDate }}</div>
          </v-flex>

          <v-flex xs3 sm3 md2 class="pt-0">
            <div class="mt-0 pt-0">
              <!-- <v-btn v-if="article.is_draft" flat small round class="warning white--text px-0 mx-0`">
                Draft
              </v-btn>
              <v-btn v-else-if="article.is_featured" flat small round class="primary white--text px-0 mx-0`">
                Featured
              </v-btn>
              <v-btn v-else flat small round class="success white--text px-0 mx-0`">
                Published
              </v-btn> -->
              <!-- <v-btn :class="[{ warning : article.is_draft}, { primary: article.is_featured }, success]"
              flat small round class="white--text px-0 mx-0`">
                Published
              </v-btn> -->
              <v-btn :class="statusClass(article)" flat small round class="white--text px-0 mx-0">
                Published
              </v-btn>
            </div>
          </v-flex>

          <v-spacer></v-spacer>

          <v-flex xs3 sm3 md2>
            <div class="mt-0 pt-0">
              <v-btn icon flat color="warning" class="pa-0 ma-0">
                <v-icon>edit</v-icon>
              </v-btn>
              <v-btn icon flat color="error" class="pa-0 ma-0">
                <v-icon>delete</v-icon>
              </v-btn>
              <v-btn icon flat color="primary" class="pa-0 ma-0">
                <v-icon>visibility</v-icon>
              </v-btn>
            </div>
          </v-flex>
        </v-layout>
        <v-divider></v-divider>
      </v-card>
    </v-container>
  </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";
// import VueMarkdown from "vue-markdown";
// import axios from "axios";

export default {
  name: "Articles",
  // components: { VueMarkdown },

  methods: {
    ...mapActions(["fetchArticles"]),
    // async tagName(tagUrl) {
    //   const response = await axios.get(tagUrl);
    //   console.log(response.data.title);
    // }

    // color the background
    statusClass(article) {
      return {
        "featured": article.is_featured,
        "warning": article.is_draft,
        "published": !article.is_featured
      }
    },

    // color a part of the component
    borderStatusCard(article) {
      return {
        "border-featured": article.is_featured,
        "border-draft": article.is_draft,
        "border-published": !article.is_featured
      }
    },
  },

  computed: mapGetters(["allArticles"]),
  created() {
    this.fetchArticles();
  }
};
</script>

<style scoped>
.published {
  background: #3cd1c2;
}
.draft {
  background: #fb8c00;
}
.featured {
  background: #1976d2;
}

.border-published {
  border-left: 4px solid #3cd1c2;
}
.border-draft {
  border-left: 4px solid #fb8c00;
}
.border-featured {
  border-left: 4px solid #1976d2;
}
</style>
