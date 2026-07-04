#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：Document_QA_Bot 
@File ：base_retriever.py
@Author ：zlh
@Date ：2026-07-01 17:43 
"""

from abc import ABC, abstractmethod


class BaseRetriever(ABC):
    @abstractmethod
    def retrieve(self, query: str):
        pass

