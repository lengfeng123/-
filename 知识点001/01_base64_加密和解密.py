#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author ZhangSir
# @date 2022/11/19
# @file 01_base64_加密和解密.py

"""
什么是base64？
base64是一种基于64个可打印字符，来表示二进制数据的方法
"""

"""
2、python中的base64模块
Base64模块真正用得上的方法只有8个，分别是：

encode, decode为一组, 专门用来编码和解码文件的, 也可以对StringIO里的数据做编解码；

encodestring, decodestring为一组，专门用来编码和解码字符串

b64encode, b64decode为一组, 用来编码和解码字符串，并且有一个替换符号字符的功能

因为Base64编码后的字符除了英文字母和数字外还有三个字符’ + / =‘,其中’=‘只是为了补全编码后的字符数为4的整数，而’+‘和’/‘在一些情况下需要被替换的，b64encode和b64decode正是提供了这样的功能。至于什么情况下’+‘和’/'需要被替换，最常见的就是对url进行Base64编码的时候。

urlsafe_b64decode, urlsafe_b64encode为一组，这个就是用来专门对url进行Base64编解码的，实际上也是调用的前一组函数。

base64.b64encode()将bytes类型数据进行base64编码，返回编码后的bytes类型

base64.b64deocde()将base64编码的bytes类型进行解码，返回解码后的bytes类型

decode的作用是将其他编码的字符串转换成unicode编码

encode的作用是将unicode编码转换成其他编码的字符串
"""

"""
3、Base64有什么使用场景
Base64是一种任意二进制到文本字符串的编码方法，常用于在URL、Cookie、网页中传输少量二进制数据，
包括MIME的电子邮件及XML的一些复杂数据

unicode编码代表二进制
"""

import base64

str1 = "18701348147"

# 先把文本转换成二进制，即unicode编码
a = str1.encode("utf-8")
# 再把二进制转化成base64格式

b = base64.b64encode(a)
print("str1加密后的结果是：", b)

# 解密，先解密成二进制文件
c = base64.b64decode(b)
# 再将二进制文件，解密成原文本数据
d = c.decode("utf-8")
print("str1解密后的结果是：", d)

e = "http://www.baidu.com&a=1"
f = base64.b64encode(e.encode('utf-8'))
print("f的值是：", f)

# 先把加密后的base64文件，解密成二进制文件
g = base64.b64decode(f)
# 再把二进制文件解密成文本文件
k = g.decode("utf-8")
print(k)

print("==========")
e1 = "http://www.baidu.com&a=1"
f1 = base64.urlsafe_b64encode(e1.encode('utf-8'))
print(f1)
p1 = base64.urlsafe_b64decode(f1).decode('utf-8')
print(p1)
