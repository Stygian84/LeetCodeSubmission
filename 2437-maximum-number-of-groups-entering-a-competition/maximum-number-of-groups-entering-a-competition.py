class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        total=0
        n = len(grades)
        for i in range(1,n+1):
            total+=i
            if total>n:
                return i-1
        return 1