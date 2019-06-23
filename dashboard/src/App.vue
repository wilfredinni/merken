<template>
  <v-app class="grey lighten-4">
    <Navbar/>
    <v-content class="mb-4">
      <router-view/>
    </v-content>
  </v-app>
</template>

<script>
import Navbar from "@/components/layout/Navbar";

export default {
  name: "App",
  components: { Navbar },
};
</script>
