#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author ZhangSir
# @date 2022/11/20
# @file 02_basicConfig方法的使用.py

"""
在logging库中，可以通过basicConfig()方法，直接对日志的输出格式和方法进行配置，
以实现快速打印日志到标准输出中。

下面使用basicConfig()方法快速打印日志
"""

# 导入logging库
import logging

# 通过basicConfig()方法控制日志输出，level参数用来设置日志输出级别，
# 此例子日志级别为INFO，低于INFO级别的日志都不会被打印，
# 而format参数用来设置日志输出格式

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s - %(message)s'
)

if __name__ == '__main__':
    logging.info('有用的信息')
