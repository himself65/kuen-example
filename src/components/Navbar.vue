<template>
  <!-- 左侧按钮 -->
  <header id="mp-navbar-toggle" class="mp-navbar mp-navbar-fixed default-primary-color">
    <button type="button" id="menubutton" @click="openMenu" class="nav-left-button">
      <span class="sr-only">Toggle navigation</span>
      <span class="icon-bar" />
      <span class="icon-bar" />
      <span class="icon-bar" />
    </button>
  </header>
</template>

<script>
import bus from '../assets/js/eventBus.js'

export default {
  name: 'Navbar',
  methods: {
    openMenu () {
      store.commit('changeMenuState')
    }
  }
  // data () {
  //   return {
  //     openMenu: 0
  //   }
  // },
  // methods: {
  //   openMenu: function () {
  //     // bus.$emit('openMenuEvent', 1)
  //     alert('1')
  //   }
  // }
}
</script>

<style>
#menubutton {
  transition: 0.2s ease-out;
}
/*上方导航栏*/
.mp-navbar-fixed {
  position: fixed;
  width: 100%;
  height: auto;
  min-width: 50px;
}

.nav-left-button {
  border-radius: 70px;
  border: 0;
  z-index: 1000;
  padding: 19px 1pc;
  background: inherit;
  background-color: inherit;
  background-image: none;
}
.mp-navbar {
  clear: both;
}

/*Navbar button*/
.nav-left-button:focus + .nav-left-button-content {
  display: block;
}
.icon-bar {
  display: inherit;
  display: block;
  width: 18px;
  height: 2px;
  background-color: inherit;
  border: 1px solid;
  border-radius: 0;
  color: white;
}
.icon-bar + .icon-bar {
  margin-top: 3px;
}
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  border: 0;
}
</style>
