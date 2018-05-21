import Vue from 'vue'
import Vuex from 'vuex'
import TestData from '../utils'

Vue.use(Vuex)

// Init
let state = {
  menuOpen: false,
  darkTheme: false,
  Data: TestData,
  DarkTheme: false
}

let mutations = {
  changeMenuState: state => {
    state.menuOpen = !state.menuOpen
  }
}
export default new Vuex.Store({
  state,
  mutations
})
