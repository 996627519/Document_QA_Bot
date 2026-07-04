#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：Document_QA_Bot 
@File ：ingest_service.py
@Author ：zlh
@Date ：2026-07-03 13:09 
"""
from loader.loader_factory import LoaderFactory
from embedding.embedding_factory import EmbeddingFactory
from vector_store.vector_store_factory import VectorStoreFactory
from splitter.splitter_factory import SplitterFactory


class IngestService(object):
    @staticmethod
    def ingest_pdf(url, splitter_type, chunk_size, chunk_overlap, store_type, embedding_type):
        docs = LoaderFactory.get_loader(url).load(url)
        all_splits = SplitterFactory.get_splitter(splitter_type).split(docs, chunk_size, chunk_overlap)
        VectorStoreFactory.create(
            store_type,
            EmbeddingFactory.create(embedding_type).get_embedding_model()
        ).add_documents(all_splits)


