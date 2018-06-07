<template>
  <div class="page-container">
    <toolbar></toolbar>
    <drawer></drawer>
    <md-content>
      <slot></slot>
    </md-content>
  </div>
</template>

<style>

</style>

<script>
import Toolbar from './Toolbar.vue'
import Drawer from '../components/Drawer.vue'

export default {
  name: 'Home',
  components: {
    Toolbar,
    Drawer
  }
}
</script>
