# VueWeb

[![Build Status](https://travis-ci.org/Himself65/VueWeb.svg?branch=master)](https://travis-ci.org/Himself65/VueWeb) ![License](https://img.shields.io/badge/license-MIT-blue.svg) ![npm (custom registry)](https://img.shields.io/npm/v/npm.svg?registry_uri=https%3A%2F%2Fregistry.npmjs.com)

> A Vue.js and Django Project to make a blog

## How to Build

1.  install the dependencies, like [rest_framework](http://www.django-rest-framework.org/) or someting else.

2.  In [FrontendSettingsConf](ulb_manager/settings.py), You must change these lines (PASSWORD has hidden)

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'vueweb',
        'USER': 'root',
        'PASSWORD': '*',
        'HOST': '127.0.0.1',
    }
}
```

3.  build frontend

```bash
# open frontend
cd frontend

# install dependencies
npm install

# build
npm run build
```

4.  start backend (you should go back first)

```bash
python3 manage.py migrate

python3 manage.py runserve
```

## License

ChartRoom is available under the MIT license. See the [LICENSE](LICENSE) file for more information.
```
