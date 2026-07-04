#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：Document_QA_Bot 
@File ：agent_factory.py
@Author ：zlh
@Date ：2026-07-03 16:19 
"""
from agent.rag_agent import RagAgent
from embedding.embedding_factory import EmbeddingFactory
from llm.llm_factory import LlmFactory
from retriever.retriever_factory import RetrieverFactory
from vector_store.vector_store_factory import VectorStoreFactory


class AgentFactory:
    _cache = {}

    @classmethod
    def get_agent(cls, llm_type, retriever_type, store_type, embedding_type):
        key = (llm_type, retriever_type, store_type, embedding_type)
        if key not in cls._cache:
            cls._cache[key] = RagAgent(
                LlmFactory.get_llm(llm_type).get_llm_model(),
                RetrieverFactory.create(
                    retriever_type,
                    VectorStoreFactory.create(store_type, EmbeddingFactory.create(embedding_type).get_embedding_model())
                )).create()
        return cls._cache[key]
