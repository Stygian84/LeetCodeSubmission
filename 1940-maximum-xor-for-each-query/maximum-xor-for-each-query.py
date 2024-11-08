class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        # find non negative k < 2**maximumBit so that xor all queries + xor k is maximised
        total = 0
        for num in nums:
            total ^= num


        res = []

        max_k = (1 << maximumBit) - 1

        for num in nums[::-1]:
            res.append(total ^ max_k)

            total^=num 

        return res