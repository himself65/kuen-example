import Vue from 'vue'
import Vuex from 'vuex'
import TestData from '../utils'

Vue.use(Vuex)

// Init
let state = {
  menuOpen: false,
  darkTheme: false,
  Data: TestData
}

let mutations = {
  changeMenuState: state => {
    state.menuOpen = !state.menuOpen
    console.log(state.menuOpen)
  }
}
export default new Vuex.Store({
  state,
  mutations
})
