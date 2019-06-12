<template>
  <div>
    <v-container my-2>

      <FilterArticle/>

      <v-card flat grid-list-xl v-for="article in allArticles" :key="article.id">
        <v-layout row wrap pa-2 :class="borderStatusCard(article)">
          <v-flex xs12 md6>
            <div class="mt-0 mb-1">{{ article.title }}</div>
            <div class="caption grey--text">{{ tagName(article.tags) }}</div>
          </v-flex>

          <v-flex xs5 sm6 md2>
            <div class="caption grey--text">Publish date</div>
            <div class="mt-0 mx-0 px-0">{{ article.created_at | formatDate }}</div>
          </v-flex>

          <v-flex xs3 sm3 md2 class="pt-0">
            <div class="mt-0 pt-0">
              <v-btn :class="statusClass(article)" flat small round class="white--text px-0 mx-0">
                {{ status(article) }}
              </v-btn>
            </div>
          </v-flex>

          <v-spacer></v-spacer>

          <v-flex xs3 sm3 md2>
            <div class="mt-0 pt-0">
              <v-btn icon flat :class="statusBtnClass(article)" class="pa-0 ma-0">
                <v-icon>edit</v-icon>
              </v-btn>
              <v-btn icon flat :class="statusBtnClass(article)" class="pa-0 ma-0">
                <v-icon>delete</v-icon>
              </v-btn>
              <v-btn icon flat :class="statusBtnClass(article)" class="pa-0 ma-0">
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
import FilterArticle from "./FilterArticle";
// import axios from "axios";
// import VueMarkdown from "vue-markdown";

export default {
  name: "Articles",
  components: { FilterArticle },

  methods: {
    ...mapActions(["fetchArticles"]),

    status(article) {
      return article.is_draft ? 'Draft' : article.is_featured ? "Featured": "Published";
    },

    // list and process tag names
    tagName(tags) {
      let string = "";
      for (let tag of tags) {
        string += `#${tag} `;
      }
      return string
    },

    // color the buttons
    statusBtnClass(article) {
      return {
        "icon-featured": article.is_featured,
        "icon-draft": article.is_draft,
        "icon-published": !article.is_featured,
      }
    },

    // color the status name
    statusClass(article) {
      return {
        "featured": article.is_featured,
        "draft": article.is_draft,
        "published": !article.is_featured,
      }
    },

    // color the left border of the v-card
    borderStatusCard(article) {
      return {
        "border-featured": article.is_featured,
        "border-draft": article.is_draft,
        "border-published": !article.is_featured
      }
    },
  },

  computed: {
    ...mapGetters(["allArticles"]),
  },
  created() {
    this.fetchArticles();
  }
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

.published {
  background: #3cd1c2;
}
.draft {
  background: #ffaa2c;
}
.featured {
  background: #9652ff;
}

.border-published {
  border-left: 4px solid #3cd1c2;
}
.border-draft {
  border-left: 4px solid #ffaa2c;
}
.border-featured {
  border-left: 4px solid #9652ff;
}
</style>
