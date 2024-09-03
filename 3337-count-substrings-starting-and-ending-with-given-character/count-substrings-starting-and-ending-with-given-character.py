class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        
        count = 1
        total = 0
        for letter in s:
            if letter==c:
                total+=count
                count+=1
        
        return total