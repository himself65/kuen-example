<template>
  <v-app id="inspire">
    <!-- NavBar部分 -->
    <v-navigation-drawer class="white" fixed v-model="vuexData.menuOpen" app>
      <drawer></drawer>
    </v-navigation-drawer>
    <toolbar></toolbar>
    <!-- Content部分 -->
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
import Toolbar from '../components/Toolbar'
import store from '../store/index'

export default {
  name: 'Home',
  components: {
    ArticleCard,
    Drawer,
    HimFooter,
    Toolbar
  },
  data: () => {
    return ({
      user: null,
      page: 1,
      articles: [],
      vuexData: store.state
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
