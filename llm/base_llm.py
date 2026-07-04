#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：Document_QA_Bot 
@File ：base_llm.py
@Author ：zlh
@Date ：2026-07-02 16:14 
"""

from abc import ABC, abstractmethod



class BaseLLM(ABC):
    @abstractmethod
    def get_llm_model(self):
        pass

