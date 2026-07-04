#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：Document_QA_Bot 
@File ：rag_agent.py
@Author ：zlh
@Date ：2026-07-02 16:20 
"""
from agent.tools import create_retrieve_tool
from langchain.agents import create_agent
from agent.prompts import RAG_PROMPT


class RagAgent:
    def __init__(self, llm, retriever):
        self.llm = llm
        self.retriever = retriever

    def create(self):
        """

        :rtype: object
        """
        tool = create_retrieve_tool(self.retriever)
        tools = [tool]
        return create_agent(model=self.llm, tools=tools, system_prompt=RAG_PROMPT)
