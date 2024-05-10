# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 0 
        right = n-1
        while left <= right:
            mid = (left+right)//2
            if isBadVersion(mid):
                if isBadVersion(mid+1):
                    right = mid-1
                if isBadVersion(mid-1)==False:
                    return mid
            else:
                if isBadVersion(mid+1):
                    return mid+1
                else:
                    left=mid+1




        