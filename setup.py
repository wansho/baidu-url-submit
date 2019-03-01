#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019/3/1 10:29
# @Author  : wansho
# @File    : setup.py

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "baidu-url-submit",
    version = "1.0.0",
    author = "wansho",
    author_email = "wanshojs@hotmail.com",
    description = "submit url to baidu.",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/wansho/baidu-url-submit",
    packages = setuptools.find_packages(),
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)