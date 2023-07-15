# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 09:04:36 2020

@author: leiya
"""


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        hash_map = {}
        for word in words:
            if word in hash_map:
                hash_map[word] +=1
            else:
                hash_map[word] =1
        
        heap = [(word,freq) for word,freq in hash_map.items()]

        def change_heap(arr,heapsort,root):
            left , right ,tmp = 2*root + 1, 2*root + 2, root
            # 比较哈希表值大小，一样则比较字母大小
            if left < heapsort and (arr[left][1] > arr[tmp][1] or (arr[left][1] == arr[tmp][1] and arr[left][0] < arr[tmp][0]) ):
                tmp = left
            if right < heapsort and  (arr[right][1] > arr[tmp][1] or (arr[right][1] == arr[tmp][1] and arr[right][0] < arr[tmp][0]) ):
                tmp = right
            if tmp != root:
                arr[root],arr[tmp] = arr[tmp], arr[root]
                change_heap(arr,heapsort,tmp)

                
        
        def build_heap(arr):
            heapsort = len(arr)
            for i in range((heapsort)//2,-1,-1):
                change_heap(arr,heapsort,i)
        
        def heap_sort(arr,k):
            build_heap(arr)
            res = []
            ans = 1
            for i in range(len(arr)-1,-1,-1):
                res.append(arr[0][0])
                arr[0],arr[i] = arr[i],arr[0]
                change_heap(arr,i,0)
                if ans == k:
                    return res
                else:
                    ans +=1
            return res
        return heap_sort(heap,k)