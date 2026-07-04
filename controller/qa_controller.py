#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：Document_QA_Bot 
@File ：qa_controller.py
@Author ：zlh
@Date ：2026-07-03 13:58 
"""
from service.ingest_service import IngestService
from service.qa_service import QAService
import configparser
import os

config_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config', 'config.ini')
config = configparser.ConfigParser()
config.read(config_path, encoding='utf-8')


def ingest_document():
    """仅在第一次存储数据到向量数据库时使用"""
    document_path = config.get('path', 'document_path')
    chunk_size = config.getint('split', 'chunk_size')
    chunk_overlap = config.getint('split', 'chunk_overlap')
    store_type = config.get('store', 'store_type')
    embedding_type = config.get('embedding', 'embedding_type')
    splitter_type = config.get('splitter', 'splitter_type')
    IngestService.ingest_pdf(
        url=document_path,
        splitter_type=splitter_type,
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        store_type=store_type,
        embedding_type=embedding_type)


def qa_controller():
    llm_type = config.get('llm', 'llm_type')
    retriever_type = config.get('retriever', 'retriever_type')
    store_type = config.get('store', 'store_type')
    embedding_type = config.get('embedding', 'embedding_type')
    qa = QAService(llm_type, retriever_type, store_type, embedding_type)
    qa.ask("简单介绍一下一站式卫生流体工程技术解决方案")


if __name__ == '__main__':
    # ingest_document()
    qa_controller()
