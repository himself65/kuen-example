<template>
  <div id="toolbar" class="mp-toolbar secondary-text-color default-primary-color">
    <div id="toolbar-content">
      <div class="icons">
        <a target="_blank" href="">
          <i class="icon qq link"></i>
        </a>
        <a target="_blank" href="https://github.com/Himself65">
          <i class="icon github link"></i>
        </a>
      </div>
      <p class="copyright">©. 2018. ChartRoom. All reights reversed.</p>
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
  box-sizing: border-box;
  position: absolute;
  bottom: 0;
  width: 100%;
  margin-top: 70px;
  text-align: center;
  color: white;
  border-bottom: 6px;
}

#toolbar-content {
  background-color: rgb(112, 112, 113);
  display: block;
  min-height: 170px;
  max-height: 270px;
  margin-top: 5px;
  margin-bottom: 5px;
  text-align: center;
  font-size: 12px;
}
#toolbar-content::after {
  content: '';
  display: block;
}

#toolbar-content .icons {
  padding-top: 5px;
  margin-left: 12px;
}

#toolbar-content .icon {
  display: inline-block;
  margin-right: 10px;
  font-size: 1.7em;
  color: white;
  border-radius: 500em !important;
  line-height: 2em !important;
  box-shadow: 0 0 0 0.1em white inset;
  width: 2em !important;
  height: 2em !important;
}

.author {
  padding-top: 5px;
  display: block;
  color: whitesmoke;
}

.copyright {
  position: absolute;
  width: 100%;
  bottom: 7px;
  display: block;
  color: rgba(255, 255, 255, 0.5);
  height: 24px;
  line-height: 24px;
  font-size: 14px;
}
</style>
