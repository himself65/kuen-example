<template>
  <div>
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
  </div>
</template>

<script>
import config from '../config'

export default {
  name: 'Drawer',
  props: {
    user: {
      default: {}
    }
  },
  data: function () {
    return {
      nav_list: []
    }
  },
  mounted: function () {
    let _this = this
    this.$nextTick(function () {
      _this.nav_list = config.themeConfig.nav
    })
  }
}
</script>

<style scoped>

</style>
