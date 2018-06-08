<template>
  <v-toolbar color="light-blue" dark fixed app scroll-off-screen>
    <v-toolbar-side-icon @click.stop="changeMenuState"></v-toolbar-side-icon>
    <v-toolbar-title>VueWeb</v-toolbar-title>
    <v-spacer></v-spacer>
    <v-menu bottom min-width="300px" offset-y>
      <v-btn slot="activator" flat fab left transition="slide-y-transition" icon>
        <v-avatar size="32">
          <img src="https://cdn.luogu.org/upload/usericon/72813.png">
        </v-avatar>
      </v-btn>
      <v-list>
        <template v-for="(item,index) in items">
          <v-list-tile class="black-link list-title-fixed" v-if="item.title" :key="item.title"
                       :href="item.url">
            {{item.title}}
          </v-list-tile>
          <v-divider v-if="item.divider" :key="index"></v-divider>
          <v-subheader v-if="item.header" :key="item.header">{{item.header}}</v-subheader>
        </template>
      </v-list>
    </v-menu>
  </v-toolbar>
</template>

<script>
import store from '../store/index'

export default {
  name: 'Toolbar',
  data () {
    return {
      items: [
        {
          header: '仪表盘'
        },
        {
          title: '个人主页',
          url: '#'
        },
        {
          title: '隐私和设置',
          url: '#'
        },
        {
          divider: true
        },
        {
          header: '我'
        },
        {
          title: '我的博客',
          url: '#'
        },
        {
          title: '我的比赛',
          url: '#'
        },
        {
          divider: true
        },
        {
          header: '账户'
        },
        {
          title: '锁定账户',
          url: '#'
        },
        {
          title: '注销',
          url: '#'
        }
      ]
    }
  },
  methods: {
    changeMenuState: function () {
      store.commit('changeMenuState')
    }
  }
}
</script>

<style scoped>
  black-link {
    color: #333 !important;
  }

  list-title-fixed {
    font-size: 14px !important;
    height: 40px !important;
  }
</style>
