#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：Document_QA_Bot 
@File ：tools.py
@Author ：zlh
@Date ：2026-07-02 16:20 
"""
from langchain.tools import tool


def create_retrieve_tool(retrieve):
    @tool(response_format="content_and_artifact")
    def retrieve_context(query: str):
        """从知识库检索相关内容"""
        docs = retrieve.retrieve(query)
        serialized = "\n\n".join(
            f"Source: {doc.metadata}\nContent: {doc.page_content}"
            for doc in docs
        )
        return serialized, docs
    return retrieve_context
