class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        l=0
        r=len(s)-1
        def isPalindromeRange(s, left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        while l<=r:
            if s[l]!=s[r]:
                return isPalindromeRange(s, l + 1, r) or isPalindromeRange(s, l, r - 1)
            else:
                l+=1
                r-=1
        return True