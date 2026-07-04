#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：Document_QA_Bot 
@File ：markdown_loader.py
@Author ：zlh
@Date ：2026-06-20 15:45 
"""
from pathlib import Path
from langchain_core.documents import Document
from loader.base_loader import DocumentBaseLoader


class MarkdownLoader(DocumentBaseLoader):
    def load(self, path):
        text = Path(path).read_text(
            encoding="utf-8"
        )
        return [
            Document(
                page_content=text,
                metadata={
                    "source": path
                }
            )
        ]
