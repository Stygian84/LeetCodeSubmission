class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i,j=0,0
        median_ptr=0

        two=False
        n,m=len(nums1),len(nums2)
        median_ptr=(n+m)//2+1

        if (n+m)%2!=1:
            two=True

        res=[]
        length=1
        while i<n or j<m:
            if i<n and j<m:
                if nums1[i]<nums2[j]:
                    res.append(nums1[i])
                    i+=1
                else:
                    res.append(nums2[j])
                    j+=1
            else:
                if i<n:
                    res.append(nums1[i])
                    i+=1
                else:
                    res.append(nums2[j])
                    j+=1

            if length==median_ptr:
                if two:
                    return (res[-1]+res[-2])/2
                return res[-1]
            length+=1
            
        return -1