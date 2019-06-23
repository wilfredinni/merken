<template>
  <nav>
    <v-toolbar flat app>
      <v-toolbar-side-icon class="grey--text"></v-toolbar-side-icon>

      <router-link to="/">
        <v-btn flat>
          <v-toolbar-title class="text-uppercase grey--text">
            <span class="font-weight-light">Merken-</span>
            <span>Dashboard</span>
          </v-toolbar-title>
        </v-btn>
      </router-link>

      <router-link to="new">
        <v-btn color="grey" flat>New</v-btn>
      </router-link>

      <router-link to="/about">
        <v-btn color="grey" flat>About</v-btn>
      </router-link>

      <v-spacer></v-spacer>

      <!-- <router-link to="/about">
        <v-btn color="grey" flat>About</v-btn>
      </router-link> -->

      <v-avatar>
        <img src="https://avatars2.githubusercontent.com/u/23016174?s=460&v=4" alt="John">
      </v-avatar>

    </v-toolbar>
  </nav>
</template>