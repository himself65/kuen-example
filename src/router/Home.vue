<template>
  <v-app id="inspire">
    <!-- NavBar部分 -->
    <v-navigation-drawer
      class="white"
      fixed
      v-model="drawer"
      app
    >
      <v-list class="light-blue" dense>
        <v-list-tile class="pl-2" avatar>
          <v-list-tile-avatar>
            <img src="https://cdn.luogu.org/upload/usericon/72813.png">
          </v-list-tile-avatar>
          <v-list-tile-content>
            <v-list-tile-title>扩散性百万甜面包</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>
      </v-list>
      <v-list dense>
        <v-list-tile v-on:click="open_url()">
          <v-list-tile-action class="pl-2">
            <v-icon>home</v-icon>
          </v-list-tile-action>
          <v-list-tile-content>
            <v-list-tile-title>Home</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>
        <!---->
        <v-list-tile v-on:click="open_url()">
          <v-list-tile-action class="pl-2">
            <v-icon>announcement</v-icon>
          </v-list-tile-action>
          <v-list-tile-content>
            <v-list-tile-title>About</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>
      </v-list>
    </v-navigation-drawer>
    <!-- ToolBar部分 -->
    <v-toolbar color="light-blue" dark fixed app>
      <v-toolbar-side-icon @click.stop="drawer=!drawer"></v-toolbar-side-icon>
      <v-toolbar-title>VueWeb</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-menu bottom min-width="300px" offset-y>
        <v-btn slot="activator" flat fab left>
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
