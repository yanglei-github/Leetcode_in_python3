# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 13:39:13 2020

@author: leiya
"""


class LRUCache:
    from collections import OrderedDict
    def __init__(self, capacity: int):
        self.maxsize = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        #若在缓存中,将其移动adict的尾部,表示最近刚用过
        if key in self.cache:
            self.cache.move_to_end(key)
        #若不再缓存中，直接返回-1，这就是get的好处
        return self.cache.get(key, -1)
        
    def put(self, key: int, value: int) -> None:
        # 如果在cache中,删掉重新赋值
        if key in self.cache:
            del self.cache[key]
        # 在字典尾部添加
        self.cache[key] = value
        #若cache超了，把最前面的内容删除除掉
        if len(self.cache) > self.maxsize:
            # last=False表示先进先出，即弹出最前面的内容
            self.cache.popitem(last = False)