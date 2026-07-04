#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：Document_QA_Bot 
@File ：splitter_factory.py
@Author ：zlh
@Date ：2026-07-03 15:26 
"""
from splitter.recursive_splitter import RecursiveSplitter


class SplitterFactory:
    @staticmethod
    def get_splitter(splitter_type):
        if splitter_type == "recursive":
            return RecursiveSplitter()
        raise ValueError(f"未知splitter{splitter_type}")
