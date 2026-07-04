#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：Document_QA_Bot 
@File ：inner_memory_store.py
@Author ：zlh
@Date ：2026-06-20 16:12 
"""
from vector_store.base_vector_store import BaseVectorStore
from langchain_core.vectorstores import InMemoryVectorStore


class InnerMemoryStore(BaseVectorStore):

    def __init__(self, embedding):
        self.store = InMemoryVectorStore(embedding)

    def add_documents(self, docs):
        self.store.add_documents(docs)

    def similarity_search(self, query, k=5):
        return self.store.similarity_search(query, k=k)

    def as_retriever(self):
        return self.store.as_retriever()
