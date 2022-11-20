#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author ZhangSir
# @date 2022/11/20
# @file 例140_字符计数.py

"""
对字符串中的字符进行计数，返回hashmap。key为字符，value是这个字符出现的次数。
输入str="abca",输出{"a":2,"b":1,"c":1}.
输入str="ab",输出{"a":1,"b":1}
"""


class Solution:
    def count_characters(self, str):
        map1 = dict()  # 先定义一个空字典
        print(map1)

        # 遍历字符串
        for i in str:
            # get(key,default = None)
            # 意思是，返回指定的键的值，如果键不存在，则返会 default 的值
            map1[i] = map1.get(i, 0) + 1
            print(map1[i])
        return map1


if __name__ == '__main__':
    str = "abca"
    solution = Solution()
    q = solution.count_characters(str)
    print(q)
