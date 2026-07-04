#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：Document_QA_Bot 
@File ：bge_embedding.py
@Author ：zlh
@Date ：2026-06-20 15:48 
"""
from embedding.base_embedding import BaseEmbedding
from langchain_huggingface import HuggingFaceEmbeddings


class BgeEmbedding(BaseEmbedding):
    def get_embedding_model(self):
        embeddings = HuggingFaceEmbeddings(
            model_name="BAAI/bge-m3"
        )
        return embeddings
