#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019/2/28 21:47
# @Author  : wansho
# @File    : submit.py

import json
import urllib.request as request

def submit(site, token, urls):
    """submit url to baidu
    :param site: a site verified on the search resource platform(https://ziyuan.baidu.com/),
                for example: blog.wansho.cn
    :param token: token applied from(https://ziyuan.baidu.com/) to submit url
    :return submit_result: number of urls successfully pushed
    """
    submit_result = 0
    url_list = []
    if type(urls) == type(""):
        url_list.append(urls)
    elif type(urls) == type([]):
        url_list = urls
    else:
        print("parameter must be a url or a url_list")
        return submit_result

    baidu_submit_api = "http://data.zz.baidu.com/urls?site={site}&token={token}".format(
        site = site, token = token)

    req = request.Request(baidu_submit_api, "\n".join(url_list).encode("utf-8"), {'Content-Type': 'text/plain'})
    retdata = {}
    try:
        reponse_baidu = request.urlopen(req)
        retdata = json.loads(reponse_baidu.read())
    except Exception as e:
        print(e)
    submit_result = retdata.get("success", 0)
    return submit_result


if __name__ == "__main__":
    site = "blog.wansho.cn"
    token = "xxx"
    urls = [
        "http://blog.wansho.cn/opinion/notes.html",
        "http://blog.wansho.cn/reading/movie-top.html",
        ]

    print(submit(site, token, urls))
