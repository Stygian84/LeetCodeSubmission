class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        if not t:
            return False
        left_s=0
        right_s=len(s)-1
        left_t=0
        right_t=len(t)-1

        while left_t<right_t:
            if s[left_s]==t[left_t]:
                left_s+=1
            if s[right_s]==t[right_t]:
                right_s-=1
            left_t+=1
            right_t-=1
        if s[left_s]==t[left_t]: #for even length of s
            left_s+=1
        
        return left_s>right_s
        '''idx=0
        if s=="":
            return True
        for letter in t:
            if idx>len(s)-1:
                break
            if s[idx]==letter:
                idx+=1
                continue
        if (idx)!=len(s):
            return False
        else:
            return True'''