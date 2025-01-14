class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        n = len(nums1)
        m = len(nums2)

        j = n-m-1
        k = m-1

        for i in range(n-1,-1,-1):
            if j>=0 and k>=0:
                if nums2[k]>nums1[j]:
                    nums1[i] = nums2[k]
                    k-=1
                else:
                    nums1[i] = nums1[j]
                    j-=1
            else:
                if j>=0:
                    nums1[i] = nums1[j]
                    j-=1
                elif k>=0:
                    nums1[i] = nums2[k]
                    k-=1