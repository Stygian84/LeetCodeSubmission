class Solution:
    def minOperations(self, nums: List[int]) -> int:
        freq = Counter(nums)

        count = 0
        print(freq)
        for k,v in freq.items():
            while v%3!=0:
                v-=2
                count+=1
                if v==0:
                    break
                if v<0:
                    return -1
            if v>0:
                count+=v//3
        return count