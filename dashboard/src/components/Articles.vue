<template>
  <div>
    <v-container my-2>
      <FilterArticle/>
      <listArticles/>
    </v-container>
  </div>
</template>

<script>
import FilterArticle from "./FilterArticle";
import listArticles from "./ListArticles";

export default {
  name: "Articles",
  components: { FilterArticle, listArticles }
};
</script>

