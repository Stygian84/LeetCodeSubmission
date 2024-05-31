class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        '''
        dc={}
        for item in nums:
            dc[item]=dc.get(item,0)+1
        res=[]
        for key,values in dc.items():
            if values==1:
                res.append(key)
        return res
        '''
        # Step 1: Calculate XOR of all elements
        xor_val = 0
        for num in nums:
            xor_val ^= num
        
        # Step 2: Find the rightmost set bit of xor_val
        rightmost_set_bit = xor_val & -xor_val
        
        # Step 3: Partition elements into two groups based on the rightmost set bit
        unique1 = 0
        unique2 = 0
        for num in nums:
            if num & rightmost_set_bit:
                unique1 ^= num
            else:
                unique2 ^= num
        
        return [unique1, unique2]