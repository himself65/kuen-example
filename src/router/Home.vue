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
    <v-toolbar color="blue" dark fixed app>
      <v-toolbar-side-icon @click.stop="drawer = !drawer"></v-toolbar-side-icon>
      <v-toolbar-title>文章列表</v-toolbar-title>
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
    <v-footer color="blue" app inset>
      <span class="white--text">&copy; 2018 Code by Himself65</span>
    </v-footer>
  </v-app>
</template>

<style>
</style>

<script>
import api from '../utils/api'
import ArticleCard from '../components/ArticleCard'

export default {
  name: 'Home',
  components: {ArticleCard},
  comments: {
    ArticleCard
  },
  data: () => {
    return ({
      articles: [],
      drawer: false
    })
  },
  methods: {
    open_url: function (url) {
      if (url === undefined) {
        // @TODO
        // 提醒用户您啥也没写
      } else {
        // @TODO
        // 跳转链接
      }
    },
    alert: function (msg) {
      // @TODO
      // 后期改到全局方法
    },
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
