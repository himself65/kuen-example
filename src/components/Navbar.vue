<template>
  <header id="mp-navbar-toggle" class="mp-navbar mp-navbar-fixed default-primary-color">
    <button type="button" class="nav-left-button">
      <span class="sr-only">Toggle navigation</span>
      <span class="icon-bar" />
      <span class="icon-bar" />
      <span class="icon-bar" />
    </button>
    <div class="nav-left-button-content">
      <li> Page </li>
      <li> About </li>
      <li> More </li>
    </div>
  </header>
</template>

<script>
export default {
  name: 'Navbar'
}
</script>

<style>
.nav-left-button-content {
  display: none;
  position: absolute;
  min-width: 168px;
  box-shadow: 0px 8px 16px 0px rgba(0, 0, 0, 0.2);
  background-color: #f9f9f9;
}
.mp-navbar-fixed {
  position: fixed;
  width: 100%;
  height: auto;
}
.nav-left-button {
  border: 0;
  position: relative;
  padding: 19px 1pc;
  background: inherit;
  background-color: inherit;
  background-image: none;
}
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
