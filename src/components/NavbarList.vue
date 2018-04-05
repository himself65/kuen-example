<template>
  <div id="menu" class="mp-navbarlist default-primary-color">
    <div id="menu-title">
      <h1> ChartRoom </h1>
    </div>
    <div id="menu-list" v-on:click="openMenu" class="navbarlist primary-text-color">
      <a href="#"> 主页 </a>
      <a href="#"> 设置 </a>
      <a href="#"> 关于 </a>
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
  font-family: Lato, 'Helvetica Neue', Arial, Helvetica, sans-serif;
}

#menu-title {
  height: auto;
  width: 100%;
  text-align: center;
  color: #011935;
}

.navbarlist {
  float: left;
  padding-top: 10px;
  padding-left: 30px;
}

.navbarlist a {
  display: block;
  padding: 0 0.2em;
  margin: 10px 15px 10px 15px;
  text-align: center;
  text-decoration: none;
  font-size: 1em;
}

.navbarlist a {
  color: #d0e9ff;
}

/* .navbarlist a:hover {
  color: rgb(88, 133, 255);
} */
</style>
