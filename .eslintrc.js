// https://eslint.org/docs/user-guide/configuring

module.exports = {
  root: true,
  parserOptions: {
    parser: 'babel-eslint'
  },
  env: {
    browser: true,
  },
  extends: [
    // https://github.com/vuejs/eslint-plugin-vue#priority-a-essential-error-prevention
    // consider switching to `plugin:vue/strongly-recommended` or `plugin:vue/recommended` for stricter rules.
    'plugin:vue/essential',
    'plugin:vue/base',
    'eslint:recommended',
    // https://github.com/standard/standard/blob/master/docs/RULES-en.md
    'standard'
  ],
  // required to lint *.vue files
  plugins: [
    'vue'
  ],
  // add your custom rules here
  rules: {
    // allow async-await
    'generator-star-spacing': 'off',
    // allow debugger during development
    'no-debugger': process.env.NODE_ENV === 'production' ? 'error' : 'off',
    // 2空格缩进 auto
    "indent": [
      "error",
      2
    ],
    // unix 换行风格 auto
    "linebreak-style": [
      "error",
      "unix"
    ],
    // 强制单引号 auto
    "quotes": [
      "error",
      "single"
    ],
    // 禁止分号 auto
    "semi": [
      "error",
      "never"
    ],
    // 变量定义或参数声明未使用
    "no-cond-assign": [
      "warn"
    ],
    // 强制 !== 和 ===, 和 null 或 undefined 比较例外
    "eqeqeq": [
      "error",
      "allow-null"
    ],
    // 强制大括号风格 auto
    "curly": [
      "error",
      "all"
    ],
    // 强制末尾换行 auto
    "eol-last": [
      "error"
    ],
    // 关键字空格 auto
    "keyword-spacing": [
      "error",
      {
        "before": true,
        "after": true
      }
    ]
  }
}
