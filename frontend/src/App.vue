<template>
  <router-view/>
</template>

<style>
#app,
html,
body {
  height: 100%;
  width: 100%;
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
a {
  color: #ffffff;
}
a:hover {
  color: #bdbdbd;
}
.dark-primary-color {
  background: #0288d1;
}
.default-primary-color {
  background: #03a9f4;
}
.light-primary-color {
  background: #b3e5fc;
}
.text-primary-color {
  color: #ffffff;
}
.accent-color {
  background: #4caf50;
}
.primary-text-color {
  color: #212121;
}
.secondary-text-color {
  color: #757575;
}
.divider-color {
  border-color: #bdbdbd;
}
</style>

<script>
export default {
  name: 'App'
}
</script>
