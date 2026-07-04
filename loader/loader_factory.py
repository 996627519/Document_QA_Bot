#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：Document_QA_Bot 
@File ：loader_factory.py
@Author ：zlh
@Date ：2026-06-20 15:35 
"""
from pathlib import Path

from loader.pdf_loader import PDFLoader
from loader.markdown_loader import MarkdownLoader


class LoaderFactory:
    @staticmethod
    def get_loader(file_path):

        suffix = Path(file_path).suffix.lower()

        if suffix == ".pdf":
            return PDFLoader()

        if suffix == ".md":
            return MarkdownLoader()

        raise ValueError(
            f"不支持的文件类型: {suffix}"
        )
