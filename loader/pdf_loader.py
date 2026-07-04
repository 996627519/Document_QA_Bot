#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：Document_QA_Bot 
@File ：pdf_loader.py
@Author ：zlh
@Date ：2026-06-20 15:45 
"""
from langchain_community.document_loaders import PyPDFLoader
from loader.base_loader import DocumentBaseLoader


class PDFLoader(DocumentBaseLoader):
    def load(self, path):
        loader = PyPDFLoader(path)
        docs = loader.load()
        return docs