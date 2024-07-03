class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        n = len(s)
        
        def is_palindrome(end):
            return s[:end+1]==s[:end+1][::-1]

        if is_palindrome(n-1):
            return s

        longest_palindrome_end = 0
        for i in range(n - 1, -1, -1):
            if is_palindrome(i):
                longest_palindrome_end = i
                break
        
        
        suffix = s[longest_palindrome_end + 1:]
        return suffix[::-1] + s
        
        '''left=[]
        right=[]

        i,j=0,len(s)-1

        while i<j:
            if s[i]==s[j]:
                left.append(s[i])
                right.append(s[j])
                i+=1
                j-=1
            else:
                left.append(s[j])
                right.append(s[j])
                j-=1
            print(left,right)
        print(left,right)
        left.append(s[i])
        print(left,right)

        left.extend(right[::-1])

        return "".join(left)
        '''