<template>
  <v-container my-2>
    <FilterArticle/>
    <listArticles/>
  </v-container>
</template>

<script>
import FilterArticle from "@/components/articles/FilterArticle";
import listArticles from "@/components/articles/ListArticles";

export default {
  name: "Articles",
  components: { FilterArticle, listArticles }
};
</script>
