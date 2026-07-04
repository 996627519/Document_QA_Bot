#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：Document_QA_Bot 
@File ：llm_factory.py
@Author ：zlh
@Date ：2026-07-03 13:33 
"""
from llm.deepseek import Deepseek


class LlmFactory:
    _cache = {}

    @classmethod
    def get_llm(cls, model_name):
        if model_name == 'deepseek':
            if model_name not in cls._cache:
                cls._cache[model_name] = Deepseek()
            return cls._cache[model_name]
        raise ValueError(f"未知模型{model_name}")