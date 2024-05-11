class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result=[]
        if len(nums1)>len(nums2):
            for item in nums2:
                if item in nums1:
                    result.append(item)
                    nums1.remove(item)
        else:
            for item in nums1:
                if item in nums2:
                    result.append(item)
                    nums2.remove(item)

        return result