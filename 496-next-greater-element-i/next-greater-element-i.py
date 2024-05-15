class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dc={}
        for i in range(len(nums2)):
            if nums2[i+1:]==[]:
                dc[nums2[i]]=-1
                continue
            for item in nums2[i+1:]:
                if item>nums2[i]:
                    dc[nums2[i]]=item
                    break
        result=[]
        for item in nums1:
            result.append(dc.get(item,-1))
        return result
        '''
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
        '''