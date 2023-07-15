# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 09:13:05 2020

@author: leiya
"""


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #quick sort从大到小排序
        def quick_sort(nums,head,tail):
            if head >= tail:
                #真正写quick_sort的时候这里需要返回Nums
                return nums
            #为了避免nums本身有序导致快排失效，partition起到不应该有的分而治之，减治的效果，时间复杂度降至0n2
            random_index = random.randint(head,tail)
            nums[random_index], nums[head] = nums[head], nums[random_index]
            pivot = nums[head]
            low = head
            high = tail
            while low < high:
                while low < high and nums[high] <= pivot:
                    high -= 1
                nums[low] = nums[high]
                while low < high and nums[low] > pivot:
                    low += 1
                nums[high] = nums[low]
            nums[low] = pivot
            if low == k-1:
                return nums
            quick_sort(nums,head,low-1)
            quick_sort(nums,low+1,tail)
            return nums
        res = quick_sort(nums,0,len(nums)-1)
        return res[k-1]
    
#小根堆，堆顶元素永远是堆中最小的元素
class Solution:
    import heapq
    def findKthLargest(self, nums: List[int], k: int) -> int:
        size = len(nums)
        L = []
        for index in range(k):
            heapq.heappush(L,nums[index])
        for index in range(k,size):
            top = L[0]
            if nums[index] > top:
                #弹出并返回最小值，然后将heapqreplace方法中item的值插入到堆中
                heapq.heapreplace(L,nums[index])
        return L[0]