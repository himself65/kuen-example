<template>
  <div id="vueweb">
    <div class="mp-vueweb-mask">
      <vue-drawer-layout ref="drawerLayout" :drawer-width="300" :drawable-distance="400" @mask-click="handleMaskClick">
        <div class="drawer" slot="drawer">
          <navbar-list></navbar-list>
        </div>
        <div class="content" slot="content">
          <navbar @childEvent="handleToggleDrawer"></navbar>
          <mainArea></mainArea>
        </div>
      </vue-drawer-layout>
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
button:focus {
  outline: none;
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
  /* font */
  font-size: 1.6rem;
  font-weight: 400;
  color: #212121;
  font-family: 'Segoe UI', 'Lucida Grande', Helvetica, Arial, 'Microsoft YaHei',
    FreeSans, Arimo, 'Droid Sans', 'wenquanyi micro hei', 'Hiragino Sans GB',
    'Hiragino Sans GB W3', FontAwesome, sans-serif;
}
</style>

<style scoped>
@import '../src/assets/css/palette.css';
</style>

<script>
import Navbar from './components/Navbar.vue'
import Toolbar from './components/Toolbar.vue'
import MainArea from './components/Content.vue'
import NavbarList from './components/NavbarList.vue'

export default {
  name: 'App',
  components: {
    Navbar,
    NavbarList,
    MainArea,
    Toolbar
  },
  methods: {
    handleToggleDrawer () {
      this.$refs.drawerLayout.toggle();
    },
    handleMaskClick () {
      this.$refs.drawerLayout.toggle(false);
    }
  }
}
</script>
