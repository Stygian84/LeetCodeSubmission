class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        
        ls = []
        for i in range(len(nums)):
            set_bit = bin(nums[i]).count("1")
            ls.append((nums[i],set_bit))
        print(ls)

        res = []

        current_set_bit = -1
        largest = -1
        smallest = math.inf
        for item in ls:
            num,set_bit = item
            if current_set_bit == -1:
                current_set_bit = set_bit
                smallest = num
                largest = num
                continue
            
            if set_bit==current_set_bit :
                smallest = min(smallest,num)
                largest = max(largest,num)
            
            else:
                res.append((smallest,largest))
                current_set_bit = set_bit
                smallest = num
                largest = num

        res.append((smallest,largest))
        if len(res)==1:
            return True

        print(res)
        for i in range(1,len(res)):
            if res[i-1][1]<=res[i][0]:
                continue
            else:
                return False
        return True