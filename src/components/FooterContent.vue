<template>
  <v-card
    flat
    tile
    width="100%"
    class="light-blue white--text text-xs-center"
  >
    <v-card-text>
      <v-btn
        v-for="item in toolbar"
        :key="item"
        icon
        class="mx-3 white--text"
        :href="item.link"
      >
        <v-icon size="24px">{{ item.icon }}</v-icon>
      </v-btn>
    </v-card-text>
    <v-card-text class="white--text">
      &copy;2018 — <strong>Himself65</strong>
    </v-card-text>
  </v-card>
</template>

<script>
import config from '../config'

export default {
  name: 'FooterContent',
  data: () => {
    return {
      toolbar: []
    }
  },
  methods: {},
  mounted: function () {
    let _this = this
    this.$nextTick(function () {
      _this.toolbar = config.themeConfig.toolbar
    })
  }
}
</script>

<style scoped>

</style>
