#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：Document_QA_Bot 
@File ：document_loader.py
@Author ：zlh
@Date ：2026-06-20 15:24 
"""

from langchain_core.documents import Document
from loader.base_loader import DocumentBaseLoader
import requests
import bs4


class WebPageLoader(DocumentBaseLoader):
    def load(self, url, bs_kwargs: dict | None = None):
        # 相当于curl xxx
        response = requests.get(url)
        # 如果状态码是404、500、403 则直接报错
        response.raise_for_status()
        # html解析，此处soup.get_text()返回的是文本
        soup = bs4.BeautifulSoup(response.text, "html.parser", **(bs_kwargs or {}))
        # 转换成Document
        return [Document(page_content=soup.get_text(), metadata={"source": url})]
