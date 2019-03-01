# baidu-url-submit

## Introduction
This tool help you to submit your url to baidu.

Only for python3.

The code is simple, I also use it to learn how to package python projects.

About the detail of submit url to baidu, you can visit: https://ziyuan.baidu.com/

## Install
```shell
pip install baidu-url-submit
```

## Demo

```python
import baidu_url_submit

site = "blog.wansho.cn" # your site
token = "xxx" # from https://ziyuan.baidu.com/
urls = [
        "http://blog.wansho.cn/opinion/notes.html",
        "http://blog.wansho.cn/reading/movie-top.html",
    ] # urls to submit


result = baidu_url_submit.submit(site, token, urls)
# if result == 2, it means two url submit success.
# if result < 2, it means some urls submit fail.
# 
# The reason why submit fail:
# 1. The submitted url is not the url of this site.
# 2. invalid url

```

## LICENSE

[MIT](LICENSE.txt)

