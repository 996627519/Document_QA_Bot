#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：Document_QA_Bot 
@File ：chroma_store.py
@Author ：zlh
@Date ：2026-06-20 23:01 
"""

from vector_store.base_vector_store import BaseVectorStore
from langchain_chroma import Chroma


class ChromaStore(BaseVectorStore):
    def __init__(self, embeddings, collection_name):
        self.store = Chroma(
            collection_name=collection_name,
            embedding_function=embeddings,
            persist_directory="./chroma_db")

    def add_documents(self, docs):
        self.store.add_documents(documents=docs)

    def similarity_search(self, query, k=5):
        return self.store.similarity_search(query, k=k)

    def as_retriever(self):
        return self.store.as_retriever()