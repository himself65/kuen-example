<template>
  <header class="him-navbar-toggle him-footer-fixed-top">
    <div class="left-button">
      <a href="/" class="luogu-logo"></a>
    </div>
    <button class="right-button">
      <span class="right-button-text right-icon-bars-content">导航切换</span>
      <span class="right-icon-bars right-icon-bars-content navbar-font"></span>
    </button>
  </header>
</template>

<script>
export default {
  name: 'Navbar'
}
</script>

<style>
.him-footer-fixed-top {
  position: fixed;
  right: 0;
  left: 0;
  z-index: 1000;
  top: 0;
}

.li {
  float: left;
}

.image {
  width: 50px;
  height: 50px;
}

/* navbar (on the top) */
.him-navbar-toggle {
  position: fixed;
  height: auto;
  min-height: 50px;
  width: 100%;
  z-index: 1100;
  background: #3498db;
  color: white; /* important */
  border-style: solid;
  border-width: 0 0 1px;
}

.luogu-logo {
  display: block;
  margin-right: 10px;
  height: 50px;
  width: 150px;
  background: url(../assets/luogu-logo.png) no-repeat center center;
  -webkit-background-size: 122px 40px;
  background-size: 122px 40px;
}

.left-button {
  float: left; /* important */
  padding: 0 10px;
  height: 50px;
  margin: 0px;
}

.navbar-font {
  font-size: 1.4rem;
}

.right-button {
  width: 42px;
  height: 32px;

  border-radius: 5px;
  position: relative;
  float: right;
  margin-right: 10px;
  margin-top: 8px;
  padding: 0.5em 1em;
  white-space: nowrap;
  color: white;
  background-color: #5eb95e;
  border-color: #5eb95e;
}
.right-button {
  font-size: 1.4rem;
}
.right-button-text {
  clip: rect(0, 0, 0, 0);
  width: 1px;
  height: 1px;
  margin: -1px;
  padding: 0;
  overflow: hidden;
  position: absolute;
}
.right-icon-bars-content {
  font-size: 1.4rem;
  display: inline-block;
  color: white;
}
</style>
