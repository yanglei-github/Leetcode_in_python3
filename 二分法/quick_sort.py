# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 10:16:26 2022

@author: leiya
"""


def quick_sort(ori_list, head, tail):
    if head >= tail:
        return ori_list
    pivot = ori_list[head]
    low = head
    high = tail
    while low < high:
        while low < high and ori_list[high] >= pivot:
            high -= 1
        ori_list[low] = ori_list[high]
        while low < high and ori_list[low] < pivot:
            low += 1
        ori_list[high] = ori_list[low]
    ori_list[low] = pivot
    quick_sort(ori_list, head, low-1)
    quick_sort(ori_list, low+1, tail)
    return ori_list

sorted_list = quick_sort([3,1,2,5,4,2],0,5)
print(sorted_list)