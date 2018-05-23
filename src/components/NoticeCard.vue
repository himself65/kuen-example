<template>
  <transition>
    
  </transition>
</template>

<script>
export default {
  name: "NoticeCard",
  props: {
    content: {
      type: string,
      default: ''
    },
    type: {
      type: string,
      default: 'info'
    }
  }
}
</script>
