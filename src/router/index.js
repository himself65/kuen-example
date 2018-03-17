import Vue from 'vue'
import Router from 'vue-router'
// compents
import Footer from '@/components/Footer'


// script
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Footer',
      component: Footer
    }
  ]
})
