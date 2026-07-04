#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：Document_QA_Bot 
@File ：base_vector_store.py
@Author ：zlh
@Date ：2026-06-20 16:10 
"""
from abc import ABC, abstractmethod


class BaseVectorStore(ABC):
    @abstractmethod
    def add_documents(self, docs):
        pass

    @abstractmethod
    def similarity_search(self, query, k=5):
        pass

    @abstractmethod
    def as_retriever(self):
        pass

