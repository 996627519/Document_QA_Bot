#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：Document_QA_Bot 
@File ：recursive_splitter.py
@Author ：zlh
@Date ：2026-07-03 15:24 
"""
from splitter.base_splitter import BaseSplitter
from langchain_text_splitters import RecursiveCharacterTextSplitter


class RecursiveSplitter(BaseSplitter):
    def split(self, docs, chunk_size, chunk_overlap):
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
        all_splits = text_splitter.split_documents(docs)
        return all_splits
