class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:
        
        substrings = [0]*26
        current_length = 0
        n = len(s)

        for i in range(n):
            if i>0 and ord(s[i])-ord(s[i-1])==1 or (s[i]=='a' and s[i-1]=='z'):
                current_length += 1
            else:
                current_length = 1

            idx = ord(s[i])-ord('a')
            substrings[idx] = max(substrings[idx],current_length)
        
        return sum(substrings)