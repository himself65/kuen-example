import Vue from 'vue'
import App from './App'
import store from './store'
import router from './router'
import VueMaterial from 'vue-material'
import Vuetify from 'vuetify'
import 'vue-material/dist/vue-material.min.css'
import 'vue-material/dist/theme/default.css'
import 'vuetify/dist/vuetify.min.css'

Vue.config.productionTip = false

Vue.use(Vuetify)
Vue.use(VueMaterial)

let vm = new Vue({
  el: '#app',
  router,
  store,
  components: {
    App
  },
  template: '<App/>'
})

Vue.use(vm)
