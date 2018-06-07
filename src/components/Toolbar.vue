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
        <v-list-tile-title>2</v-list-tile-title>
        <v-list-tile-title>3</v-list-tile-title>
        <v-list-tile-title>4</v-list-tile-title>
      </v-list>
    </v-menu>
  </v-toolbar>
</template>

<script>
import store from '../store/index'

export default {
  name: 'Toolbar',
  methods: {
    changeMenuState: function () {
      store.commit('changeMenuState')
    }
  }
}
</script>

<style scoped>

</style>
