#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：Document_QA_Bot 
@File ：retriever_factory.py
@Author ：zlh
@Date ：2026-07-01 19:06 
"""

from retriever.vector_retriever import VectorRetriever


class RetrieverFactory:
    @staticmethod
    def create(retriever_name, vector_store):
        if retriever_name == 'vector':
            return VectorRetriever(vector_store)
        raise ValueError("未知retriever")

