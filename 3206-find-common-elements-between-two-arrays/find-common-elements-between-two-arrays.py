class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result=[]
        count=0
        for item in nums1:
            if item in nums2 :
                count+=1
        result.append(count)
        count=0
        for item in nums2:
            if item in nums1 :
                count+=1
        result.append(count)
        return result
        
        
        