<template>
  <div id="vueweb">
    <div class="mp-vueweb-mask">
      <navbar></navbar>
      <menu></menu>
      <content></content>
      <toolbar></toolbar>
    </div>
  </div>
</template>

<style>
* {
  -webkit-box-sizing: border-box;
  box-sizing: border-box;
}

button,
input {
  margin: 0;
  font: inherit;
  color: inherit;
  outline: 0 none !important;
}
.mp-vueweb-mask {
  position: fixed;
  z-index: 9998;
  top: 0;
  left: 0;
  width: 100%;
  min-width: 100%;
  height: 100%;
  min-height: 100%;
  background-color: white;
  display: table;
  transition: opacity 0.3s ease;
}
</style>

<style scoped>
@import '../src/assets/css/palette.css';
</style>

<script>
import Navbar from './components/Navbar.vue'
import Toolbar from './components/Toolbar.vue'
import Content from './components/Content.vue'
import Menu from './components/Menu.vue'

export default {
  name: 'App',
  components: {
    Navbar,
    Menu,
    Content,
    Toolbar
  }
}
</script>
