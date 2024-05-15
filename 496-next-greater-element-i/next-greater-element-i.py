class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result=[]
        for i in range(len(nums1)):
            for idx in range(len(nums2)):
                if nums2[idx]==nums1[i]:
                    print(nums1[i],nums2[idx+1:])
                    if nums2[idx+1:]==[]:
                        result.append(-1)
                        continue
                    max_num=-1
                    for item in nums2[idx+1:]:
                        if item >nums1[i]:
                            max_num=item  
                            break  
                    result.append(max_num)
        return result