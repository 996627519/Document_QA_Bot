#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：Document_QA_Bot 
@File ：base_loader.py
@Author ：zlh
@Date ：2026-06-20 15:43 
"""
from abc import ABC, abstractmethod


class DocumentBaseLoader(ABC):
    @abstractmethod
    def load(self, path):
        """
        返回langchain document列表
        :return:
        """
        pass
