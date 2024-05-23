class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        result=[]
        dc={}
        for item in nums1:
            dc[item[0]]=dc.get(item[0],0)+item[1]
        for item in nums2:
            dc[item[0]]=dc.get(item[0],0)+item[1]
        for key,values in dc.items():
            result.append([key,values])
        result.sort()
        return result