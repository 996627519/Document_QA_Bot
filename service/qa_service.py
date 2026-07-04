#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：Document_QA_Bot 
@File ：qa_service.py
@Author ：zlh
@Date ：2026-07-03 13:28 
"""
from agent.agent_factory import AgentFactory


class QAService:
    def __init__(self, llm_type, retriever_type, store_type, embedding_type):
        self.llm_type = llm_type
        self.retriever_type = retriever_type
        self.store_type = store_type
        self.embedding_type = embedding_type
        self.rag_agent = AgentFactory.get_agent(self.llm_type, self.retriever_type, self.store_type, self.embedding_type)

    def ask(self, query):
        stream = self.rag_agent.stream_events(
            {"messages": [{"role": "user", "content": query}]},
            version="v3",
        )
        for kind, item in stream.interleave("messages", "tool_calls"):
            # 判断如果是LLM的输出，则逐token输出（流式输出）
            if kind == "messages":
                for token in item.text:
                    print(token, end="", flush=True)
            # Agent决定调用RAG检索工具
            elif kind == "tool_calls":
                print(f"\nTool call: {item.tool_name}({item.input})")
                print(f"Tool result: {item.output}")

        return stream.output

