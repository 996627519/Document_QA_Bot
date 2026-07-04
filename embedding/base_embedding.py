#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：Document_QA_Bot 
@File ：base_embedding.py
@Author ：zlh
@Date ：2026-06-20 15:44 
"""
from abc import ABC, abstractmethod


class BaseEmbedding(ABC):
    @abstractmethod
    def get_embedding_model(self):
        pass
