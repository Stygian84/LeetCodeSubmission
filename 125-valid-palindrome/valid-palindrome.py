class Solution:
    def isPalindrome(self, s: str) -> bool:

        n = len(s)
        i=0
        j=n-1

        while i<j:
            while i<n and not s[i].isalnum():
                i+=1
            while j>=0 and not s[j].isalnum():
                j-=1
            if i>=j:
                break
                
            if s[i].isnumeric() and s[j].isnumeric():
                if s[i]!=s[j]:
                    return False
                pass
            elif s[i].lower() != s[j].lower():
                return False
            i+=1
            j-=1
        
        return True