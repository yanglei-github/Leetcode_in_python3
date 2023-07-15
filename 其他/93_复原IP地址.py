# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 10:16:24 2020

@author: leiya
"""


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        size = len(s)
        if size < 4 or size > 12:
            return []
        def dfs(s, size, split_times, begin, path, res):
            if begin == size:
                if split_times == 4:
                    res.append('.'.join(path))
                return
            #此处为剪枝操作
            #split == 1表示前面已经分出了一块，马上就要分出第二块地址段了,所有这里判断的是，如果前面分出的地址段都是1的情况下后面代码不足其他块的代码
            if size - begin < (4 - split_times) * 1 or size - begin > 3 * (4 - split_times):
                return

            for i in range(3):
                if begin + i >= size:
                    break

                ip_segment = judge_if_ip_segment(s, begin, begin + i)

                if ip_segment != -1:
                    path.append(str(ip_segment))
                    dfs(s, size, split_times + 1, begin + i + 1, path, res)
                    path.pop()
        def judge_if_ip_segment(s, left, right):
            size = right - left + 1

            if size > 1 and s[left] == '0':
                return -1

            res = 0
            for i in range(left, right + 1):
                res = res * 10 + ord(s[i]) - ord('0')

            if res > 255:
                return - 1
            return res
        path = []
        res = []
        dfs(s, size, 0, 0, path, res)
        return res