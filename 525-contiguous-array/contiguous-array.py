class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        #try convert 0 to -1 and add, if equal to 0, equal
        n = len(nums)
        prefix = [0]*(n)
        
        longest = 0 #furthest 0 or length between one 0  and one -1
        
        for i in range(n):
            prefix[i]=prefix[i-1]
            if nums[i]==1:
                prefix[i]+=1
            else:
                prefix[i]-=1     

            if prefix[i]==0:
                longest = i+1
            

        # find max range prefix that are equal
        dc = defaultdict(int)

        for i in range(n):
            if prefix[i] in dc:
                longest = max(longest,i-dc[prefix[i]])
            else:
                dc[prefix[i]]=i   

        return longest