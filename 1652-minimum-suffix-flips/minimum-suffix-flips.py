class Solution:
    def minFlips(self, target: str) -> int:
        count = 0
        prev_bit = '0'

        for bit in target:
            if bit != prev_bit:
                count += 1
                prev_bit = bit

        return count

            

