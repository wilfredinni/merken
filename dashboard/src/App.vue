<template>
  <v-app class="grey lighten-4">
    <Navbar/>
    <v-content class="mb-4">
      <router-view/>
    </v-content>
  </v-app>
</template>

<script>
import Navbar from "@/components/Navbar";

export default {
  name: "App",
  components: { Navbar },
  data () {
      return {
        drawer: true,
        items: [
          { title: 'Home', icon: 'dashboard' },
          { title: 'About', icon: 'question_answer' }
        ],
        mini: true,
        right: null
      }
    }
};
</script>
