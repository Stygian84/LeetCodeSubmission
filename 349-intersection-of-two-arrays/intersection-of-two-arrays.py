class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return set.intersection(set(nums1),set(nums2))
        