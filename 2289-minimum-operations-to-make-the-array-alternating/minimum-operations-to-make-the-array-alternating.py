class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        if len(set(nums))==1:
            return len(nums)//2
        odd = defaultdict(int)
        even = defaultdict(int)

        n=len(nums)
        #num,freq
        
        for i in range(n):
            if i%2==0:
                even[nums[i]]+=1
            else:
                odd[nums[i]]+=1
        
        count = 0
        odd_ls=list(sorted(odd.items(), key = lambda x:-x[1])) + [(0,0)]
        even_ls=list(sorted(even.items(), key = lambda x:-x[1])) + [(0,0)]

        odd_num, odd_freq = odd_ls[0]
        even_num, even_freq = even_ls[0]

        if odd_num == even_num:
            if odd_ls[1][1] + even_freq > even_ls[1][1] + odd_freq:
                odd_num = odd_ls[1][0]
            else:
                even_num = even_ls[1][0]

        for i in range(n):
            if i%2==0:
                if nums[i]!=even_num:
                    count+=1
            else:
                if nums[i]!=odd_num:
                    count+=1
        return count
