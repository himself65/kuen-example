<template>
  <transition>
    <div v-show="visible">
      <slot>

      </slot>
    </div>
  </transition>
</template>

<script>
const typeMap = {
  success: 'success',
  info: 'info',
  warning: 'warning',
  error: 'error'
};

export default {
  name: "NoticeCard",
  data: {
    return: {
      message: '',
      type: typeMap.info,
      visible: false, // 是否显示组件，默认显示
    }
  },
  watch: {
    visible: function (newVal) {
      if (newVal) {
        this.visible = true;

      }
    }
  }
}
</script>
