<template>
 <div id="toolbar" class="mp-toolbar secondary-text-color">
    <div class="mp-toolbar-content">
      Hello,world
    </div>
  </div>
</template>

<script>
export default {
  name: 'Toolbar'
}
</script>

<style>
#toolbar {
    height: 40px;
    box-sizing: border-box;
    position: absolute;
    bottom: 0;
    width: 100%;
}
.mp-toolbar-content {
  text-align: center;
}
</style>
