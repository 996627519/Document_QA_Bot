#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：Document_QA_Bot 
@File ：embedding_factory.py
@Author ：zlh
@Date ：2026-06-20 15:56 
"""
from embedding.bge_embedding import BgeEmbedding


class EmbeddingFactory:

    _cache = {}

    @classmethod
    def create(cls, name):
        if name == 'bge':
            if name not in cls._cache:
                cls._cache[name] = BgeEmbedding()
            return cls._cache[name]

        raise ValueError(f'未知embedding模型: {name}')
