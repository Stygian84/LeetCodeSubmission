class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        n = len(grades)
        
        left, right = 1, n
        result = 1 
        
        while left <= right:
            mid = (left + right) // 2
            if mid * (mid + 1) // 2 <= n:
                result = mid  
                left = mid + 1 
            else:
                right = mid - 1 
        
        return result
        '''total=0
        n = len(grades)
        for i in range(1,n+1):
            total+=i
            if total>n:
                return i-1
        return 1'''