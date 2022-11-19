#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author ZhangSir
# @date 2022/11/19
# @file 01大小写转换.py

"""
将一个字符，由小写字母，转换为大写字母
输入a,输出A，输入b,输出B，
"""

# 在ASCII码中，小写字母与对应的大写字母相差32
"""
核心思想，主要用到这两个函数，一个是获取ASCII码的数值，一个是根据数值，反显ASCII字符是什么

chr(i)
参数i -- 可以是10进制也可以是16进制的形式的数字。
返回值是当前整数对应的 ASCII 字符

ord()，是用来返回一个字符的ASCII码数值的，也就是说输入一个符号可以去返回一个对应的一个十进制整数
"""


class Solution:
    def lowercaseToUpperCase(self, character):
        """

        :param character: 传要输入的小写字母
        :return: 返回的ans，相当于是大写字母
        """
        # ans = chr(ord(character) - 32)  # 一行代码即可
        a1 = ord(character)
        print(a1)
        a2 = a1 - 32
        print(a2)
        ans = chr(a2)
        return ans


if __name__ == '__main__':
    solution = Solution()
    ans = solution.lowercaseToUpperCase('c')
    print("输入的字母为:c")
    print("输出的字母为:", ans)
