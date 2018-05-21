import axios from 'axios'

/**
 * @todo
 * @param {string} url
 * @param {string} method
 * @param params like queryString. if a url is index?a=1&b=2, params = {a: '1', b: '2'}
 * @param data post data, use for method put|post
 * @returns {Promise}
 */
function ajax (url, method, params, data) {
  return new Promise((resolve, reject) => {
    axios({
      url, method, params, data
    }).then(res => {
        // CHECK IF status===20x
        if (res.data.error) {
        
        } else {
        
        }
      }
    ), res => {
      reject(res);
      Vue.prototype.$error(res.data.data);
    }
  });
}
