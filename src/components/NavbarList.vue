<template>
  <div id="menu" class="mp-navbarlist default-primary-color">
    <div id="menu-list" v-on:click="openMenu" class="navbarlist primary-text-color">
      <a href="#"> 1 </a>
      <a href="#"> 2 </a>
      <a href="#"> 3 </a>
      <a href="#"> 4 </a>
    </div>
  </div>
</template>

<script>
import bus from '../assets/js/eventBus.js'
export default {
  name: 'NavbarList',
  methods: {
    openMenu: function () {
      alert('接下来就没做了')
    }
  }
}
</script>

<style>
#menu {
  position: absolute;
  top: 0;
  bottom: 0;
  width: 300px;
  z-index: 1003;
  transition: 0.2s ease-out;
  box-shadow: 0px 8px 16px 0px rgba(0, 0, 0, 0.2);
}

.navbarlist {
  float: left;
  padding-top: 70px;
  padding-left: 30px;
}

.navbarlist a {
  display: block;
  padding: 0 0.2em;
  margin: 0 15px;
  text-align: center;
  font-size: 1.2em;
}
</style>
