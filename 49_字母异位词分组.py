# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 09:52:27 2020

@author: leiya
"""


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}
        for item in strs:
            key = tuple(sorted(item))
            dict[key] = dict.get(key, []) + [item]
        return list(dict.values())