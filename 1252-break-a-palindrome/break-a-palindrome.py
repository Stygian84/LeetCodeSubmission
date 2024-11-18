class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome)==1:
            return ""
        n = len(palindrome)
        i = 0
        j = n-1

        palindrome = list(palindrome)
        while i < j:
            if palindrome[i] == "a":
                i+=1
                j-=1
            else:
                palindrome[i] = "a"
                return "".join(palindrome)
        
        palindrome[-1] = "b"
        return "".join(palindrome)