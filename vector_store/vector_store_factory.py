#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：Document_QA_Bot 
@File ：vector_store_factory.py
@Author ：zlh
@Date ：2026-07-01 17:34 
"""

from vector_store.chroma_store import ChromaStore
from vector_store.inner_memory_store import InMemoryVectorStore


class VectorStoreFactory:
    _cache = {}

    @classmethod
    def create(cls, store_type, embedding, collection_name="knowledge"):
        key = (store_type, collection_name)
        if store_type == 'chroma':
            if key not in cls._cache:
                cls._cache[key] = ChromaStore(embedding, collection_name)
            return cls._cache[key]


        if store_type == 'memory':
            if store_type not in cls._cache:
                cls._cache[store_type] = InMemoryVectorStore(embedding)
            return cls._cache[store_type]

        raise ValueError("未知向量库")

