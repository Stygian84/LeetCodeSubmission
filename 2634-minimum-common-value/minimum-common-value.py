class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        common_elements = set(nums1) & set(nums2)
        ls=sorted(common_elements)
        if common_elements:
            return ls[0]
        else:
            return -1
        