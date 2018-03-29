<template>
  <div id="menu" class="mp-navbarlist default-primary-color">
    <div id="menu-list" class="navbarlist primary-text-color">
      <a href="#" />
    </div>
  </div>
</template>

<style>
#menu {
  position: absolute;
  top: 0;
  bottom: 0;
  left: -300px;
  width: 300px;
  transition: 0.2s ease-out;
  box-shadow: 0px 8px 16px 0px rgba(0, 0, 0, 0.2);
}

.navbarlist {
  float: left;
  padding: 2.5em 2em 0 6em;
}

.navbarlist a {
  opacity: 0;
  display: inline-block;
  padding: 0 0.2em;
  margin: 0 15px;
  text-align: center;
  font-size: 1.2em;
}
</style>

<script>
import bus from '../assets/js/eventBus.js'
export default {
  name: 'NavbarList'
}
</script>
