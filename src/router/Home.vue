<template>
  <v-app id="inspire">
    <!-- NavBar部分 -->
    <v-navigation-drawer class="white" fixed v-model="drawer" app>
      <drawer></drawer>
    </v-navigation-drawer>
    <!-- ToolBar部分 -->
    <v-toolbar color="light-blue" dark fixed app scroll-off-screen>
      <v-toolbar-side-icon @click.stop="drawer=!drawer"></v-toolbar-side-icon>
      <v-toolbar-title>VueWeb</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-menu bottom min-width="300px" offset-y>
        <v-btn slot="activator" flat fab left transition="slide-y-transition">
          <v-avatar size="32">
            <img src="https://cdn.luogu.org/upload/usericon/72813.png">
          </v-avatar>
        </v-btn>
        <v-list>
          <v-list-tile-title>2</v-list-tile-title>
          <v-list-tile-title>3</v-list-tile-title>
          <v-list-tile-title>4</v-list-tile-title>
        </v-list>
      </v-menu>
    </v-toolbar>
    <v-content>
      <v-container fluid
                   style="min-height: 0;"
                   grid-list-lg>
        <v-layout row wrap>
          <article-card v-for="article in articles" v-bind:article="article" v-bind:key="article.id"></article-card>
        </v-layout>
      </v-container>
    </v-content>
    <!-- Footer部分 -->
    <v-footer absolute class="toolbar-fix" height="auto" inset app>
      <him-footer></him-footer>
    </v-footer>
  </v-app>
</template>

<style>
  .toolbar-fix {
    position: inherit;
  }
</style>

<script>
import api from '../utils/api'
import ArticleCard from '../components/ArticleCard'
import Drawer from '../components/Drawer'
import HimFooter from '../components/FooterContent'

export default {
  name: 'Home',
  components: {
    ArticleCard,
    Drawer,
    HimFooter
  },
  data: () => {
    return ({
      user: null,
      page: 1,
      articles: [],
      drawer: false
    })
  },
  methods: {
    get_list () {
      let _this = this
      api.getAllArticles().then(function (data) {
        _this.articles = data.data
      })
    }
  },
  mounted: function () {
    let _this = this
    this.$nextTick(function () {
      _this.get_list()
    })
  }
}
</script>
