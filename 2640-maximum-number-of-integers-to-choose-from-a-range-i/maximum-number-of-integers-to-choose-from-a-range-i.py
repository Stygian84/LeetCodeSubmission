class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        s = set(banned)
        count = 0
        total = 0
        for i in range(1,n+1):
            if total+i>maxSum:
                break
            if i not in s:
                total+=i
                count+=1
        return count