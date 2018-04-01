<template>
  <!-- 左侧按钮 -->
  <div id="mp-navbar-toggle" class="mp-navbar mp-navbar-fixed default-primary-color">
    <button type="button" id="menubutton" v-on:click="openMenu" class="nav-left-button">
      <span class="sr-only">Toggle navigation</span>
      <span class="icon-bar" />
      <span class="icon-bar" />
      <span class="icon-bar" />
    </button>
  </div>
</template>

<script>
import bus from '../assets/js/eventBus.js'

export default {
  name: 'Navbar',
  methods: {
    openMenu () {
      this.$emit('childEvent', 'open')
    }
  }
}
</script>

<style>
#mp-navbar-toggle {
  top: 0;
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
