<template>
  <v-app id="inspire">
    <!-- NavBar部分 -->
    <v-navigation-drawer
      class="blue lighten-3"
      fixed
      v-model="drawer"
      app
    >
      <v-list dense>
        <!-- TODO -->
        <v-list-tile v-on:click="open_url()">
          <v-list-tile-action>
            <v-icon>home</v-icon>
          </v-list-tile-action>
          <v-list-tile-content>
            <v-list-tile-title>Home</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>
        <!-- TODO -->
        <v-list-tile v-on:click="open_url()">
          <v-list-tile-action>
            <v-icon>announcement</v-icon>
          </v-list-tile-action>
          <v-list-tile-content>
            <v-list-tile-title>About</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>
      </v-list>
    </v-navigation-drawer>
    <!-- ToolBar部分 -->
    <v-toolbar color="blue lighten-2" dark fixed app>
      <v-toolbar-side-icon @click.stop="drawer = !drawer"></v-toolbar-side-icon>
      <v-toolbar-title>VueWeb</v-toolbar-title>
    </v-toolbar>
    <v-content>
      <v-container fluid fill-height>
        <v-layout
          justify-center
          align-center
        >

        </v-layout>
      </v-container>
    </v-content>
    <!-- Footer部分 -->
    <v-footer color="blue lighten-2" app inset>
      <span class="white--text">&copy; 2018 Code by Himself65</span>
    </v-footer>
  </v-app>
</template>

<style>
</style>

<script>
export default {
  name: 'Home',
  data: () => {
    return ({
      articles: null,
      drawer: false
    })
  },
  methods: {
    open_url: function (url) {
      if (url === undefined) {
        // TODO
        // 提醒用户您啥也没写
      } else {
        // TODO
        // 跳转链接
      }
    }
  }
}
</script>
