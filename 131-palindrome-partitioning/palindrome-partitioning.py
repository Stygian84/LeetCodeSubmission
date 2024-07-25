class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(x):
            return x==x[::-1]
            
        def backtrack(start: int, path: list):
            if start == len(s):
                result.append(path[:])
                return
            for end in range(start + 1, len(s) + 1):
                substring = s[start:end]
                if isPalindrome(substring):
                    path.append(substring)
                    backtrack(end, path)
                    path.pop()
        
        result = []
        backtrack(0, [])
        return result