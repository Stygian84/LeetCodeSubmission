class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        nums1=list(set(nums1))
        nums2=list(set(nums2))
        nums1.extend(nums2)
        nums1.sort()
        for idx in range(len(nums1)-1):
            if nums1[idx]==nums1[idx+1]:
                return nums1[idx]
        return -1
        