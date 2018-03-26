import Vue from 'vue'
import Router from 'vue-router'
// compents
import Navbar from '@/components/Navbar'
import Content from '@/components/Content'
import Toolbar from '@/components/Toolbar'

// script
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Navbar',
      component: Navbar
    },
    {
      path: '/',
      name: 'Content',
      component: Content
    },
    {
      path: '/',
      name: 'Toolbar',
      component: Toolbar
    }
  ]
})
