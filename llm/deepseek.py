#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：Document_QA_Bot 
@File ：deepseek.py
@Author ：zlh
@Date ：2026-07-02 16:16 
"""
import os
from dotenv import load_dotenv
from llm.base_llm import BaseLLM
from langchain_deepseek import ChatDeepSeek

load_dotenv()


class Deepseek(BaseLLM):
    def get_llm_model(self):
        return ChatDeepSeek(
            model="deepseek-v4-flash",
            api_key=os.environ.get("api_key"),  # 从 platform.deepseek.com 获取
            max_retries=2
        )