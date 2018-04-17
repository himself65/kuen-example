import Vue from 'vue'
import Router from 'vue-router'

import Home from './Home.vue'
import Chart from './Chart.vue'
import About from './About.vue'
import Settings from './Settings.vue'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/Chart',
      name: 'Chart',
      component: Chart
    },
    {
      path: '/about',
      name: 'About',
      component: About
    },
    {
      path: '/setttings',
      name: 'Settings',
      component: Settings
    }
  ]
})
