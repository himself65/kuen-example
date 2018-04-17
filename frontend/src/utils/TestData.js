var _ = require('lodash')
const avatarURL = 'https://cdn.luogu.org/upload/usericon/72813.png'
const img = ''
var author = {
  id: 72813,
  name: 'Himself65',
  avatar: avatarURL,
  bio: 'Hell is empty'
}

var article = {
  uid: 2234,
  title: '今日市民郭嘉掉入水中，到目前为止生死未卜',
  abstract: '沟里郭嘉生死疑，起因祸复去之',
  category: ['News', 'Important'],
  headImg: img,
  rate: {
    good: 666,
    bad: 12
  }
}

var articles = (() => {
  let articles = []
  let articleGroup = {}
  articleGroup.article = article
  articleGroup.author = author
  for (let i = 1243; i < 1251; i++) {
    articleGroup.article.uid = i
    articles.push(_.cloneDeep(articleGroup))
  }
  return articles
})()

var TestData = { articles, author }

export default { TestData }
