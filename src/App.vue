<template>
  <div id="vueweb">
    <div class="mp-vueweb-mask">
      <div id="mp-vueweb-navbar">
        <navbar/>
      </div>
      <div id="mp-vueweb-content">
        <content/>
      </div>
      <div id="mp-vueweb-toolbar">
        <toolbar/>
      </div>
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
}

.mp-vueweb-mask {
  position: fixed;
  z-index: 9998;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
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

export default {
  name: 'App',
  components: {
    Navbar,
    Content,
    Toolbar
  }
}
</script>
