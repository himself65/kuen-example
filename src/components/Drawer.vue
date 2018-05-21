<template>
  <md-drawer :md-active.sync="menuState" md-persistent="full" class="him-drawer-fixed">
    <md-toolbar class="md-transparent" md-elevation="0">
      <h3>Navigation</h3>

      <div class="md-toolbar-section-end">
        <md-button class="md-icon-button md-dense" @click="toggleMenu(false)">
          <md-icon>keyboard_arrow_left</md-icon>
        </md-button>
      </div>
    </md-toolbar>

    <md-list>
      <md-list-item to="/">
        <md-icon>home</md-icon>
        <span class="md-list-item-text">主页</span>
      </md-list-item>

      <md-list-item to="/Chart">
        <md-icon>message</md-icon>
        <span class="md-list-item-text">消息</span>
      </md-list-item>

      <!-- <md-list-item to="/Settings">
        <md-icon>settings</md-icon>
        <span class="md-list-item-text">设置</span>
      </md-list-item> -->

      <md-list-item to="/About">
        <md-icon>info</md-icon>
        <span class="md-list-item-text">关于</span>
      </md-list-item>
    </md-list>
  </md-drawer>
</template>

<script>
import store from '../store'
export default {
  name: 'Drawer',
  data: function () {
    return {
      vuexData: store.state, // store状态
      menuState: false // 绑定Drawer是否开启
    }
  },
  watch: {
    'vuexData.menuOpen': {
      handler: function (value) {
        this.menuState = value
      },
      deep: true // 深度监听
    }
  },
  methods: {
    toggleMenu () {
      store.commit('changeMenuState')
    }
  }
}
</script>

<style>
.him-drawer-fixed {
  position: fixed;
  top: 0;
  left: 0;
  bottom: 0;
}
</style>
