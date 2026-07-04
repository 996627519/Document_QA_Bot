#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：Document_QA_Bot 
@File ：vector_retriever.py
@Author ：zlh
@Date ：2026-07-01 17:48 
"""
from retriever.base_retriever import BaseRetriever


class VectorRetriever(BaseRetriever):

    def __init__(self, vector_store, top_k=5):
        self.vector_store = vector_store
        self.top_k = top_k

    def retrieve(self, query: str):
        return self.vector_store.similarity_search(query, k=self.top_k)

