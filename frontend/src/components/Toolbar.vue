<template>
  <div>
    <md-toolbar class="md-primary">
      <md-button class="md-icon-button"
                 @click="toggleMenu">
        <md-icon>menu</md-icon>
      </md-button>
      <span class="md-title">VueWeb</span>
    </md-toolbar>
  </div>
</template>

<style>

</style>

<script>
import store from '../store'
export default {
  name: 'Toolbar',
  data: function () {
    return {}
  },
  methods: {
    toggleMenu () {
      store.commit('changeMenuState')
    }
  }
}
</script>
