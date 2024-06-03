class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        pointer1,pointer2,write=m-1,n-1,m+n-1

        while pointer2>=0:
            if pointer1>=0 and nums1[pointer1] > nums2[pointer2]:
                    nums1[write]=nums1[pointer1]
                    pointer1-=1
            else:
                nums1[write]=nums2[pointer2]
                pointer2-=1
            write-=1
        '''
        count=0
        for i in range(m+n):
            print(i,count)
            if nums2:
                if nums1[i]<=nums2[count]:
                    if nums1[i]==0:
                        nums1[i]=nums2[count]
                        count+=1
                    continue
                else:
                    nums1[m+count],nums1[i]=nums1[i],nums2[count]
                    count+=1
                    if count==n:
                        break
                    continue
        return nums1
        '''
