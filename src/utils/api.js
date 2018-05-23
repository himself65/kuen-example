import axios from 'axios'
// import store from '../store'

// axios.defaults.url = 'localhost:8000'
axios.defaults.baseURL = 'http://localhost:8000/api'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'
axios.defaults.xsrfCookieName = 'csrftoken'

export default {
  getArticlesByID (id) {
    return ajax(`article/${id}`, 'get', {})
  },
  getAllArticles () {
    return ajax('article/', 'get', {})
  }
}

/**
 * @param {string} url
 * @param {string} method
 * @param {{params, data}} options, params: like queryString. data: post data
 * @returns {Promise}
 */
function ajax (url, method, options) {
  if (options !== undefined) {
    var {params = {}, data = {}} = options
  } else {
    params = data = {}
  }
  return new Promise((resolve, reject) => {
    axios({
      url, method, params, data
    }).then(res => {
      // CHECK IF status===20x
      if (res.data.error) {
        reject(res)
      } else {
        resolve(res)
      }
    })
  })
}
