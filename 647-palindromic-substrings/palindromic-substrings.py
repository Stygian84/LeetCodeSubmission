class Solution:
    def countSubstrings(self, s: str) -> int:
        count=0
        n=len(s)
        def calc(s,left,right):
            count=0
            while left>=0 and right<len(s) and s[left]==s[right]:
                count+=1
                left-=1
                right+=1
            return count
        
        for mid in range(2*n-1):
            l=mid//2
            r=l+mid%2
            count+=calc(s,l,r)
        return count