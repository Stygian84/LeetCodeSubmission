class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        
        n = len(arr)
        l = 0
        r = n-1

        while l<r:
            mid = (l+r)//2
            if arr[mid]>arr[mid-1] and arr[mid]>arr[mid+1]:
                return mid
            elif arr[mid-1]>arr[mid]>arr[mid+1]:
                r=mid
            else:
                l=mid
        return -1