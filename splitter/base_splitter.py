#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：Document_QA_Bot 
@File ：base_splitter.py
@Author ：zlh
@Date ：2026-07-03 15:23 
"""
from abc import ABC, abstractmethod


class BaseSplitter(ABC):
    @abstractmethod
    def split(self, docs, chunk_size, chunk_overlap):
        pass
