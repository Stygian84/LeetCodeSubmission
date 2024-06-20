class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        n=len(s)
        if n<=1:
            return 0
        prev_count=0
        curr_count=1
        total=0

        for i in range(1,n):
            if s[i]==s[i-1]:
                curr_count+=1
            else:
                total+=min(prev_count,curr_count)
                prev_count=curr_count
                curr_count=1
        total+=min(prev_count,curr_count)
        return total