class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        res=0
        arr2.sort()
        for i in range(len(arr1)):
            left, right=0, len(arr2)-1
            flag = 0
            while left < right:
                mid=(right+left) // 2
                if arr2[mid] - arr1[i] > d:
                    right=mid-1
                elif arr2[mid] - arr1[i] < -d:
                    left = mid + 1
                else: 
                    flag = 1
                    break
            if abs(arr2[right]-arr1[i]) > d and flag == 0:
                res+=1
        return res