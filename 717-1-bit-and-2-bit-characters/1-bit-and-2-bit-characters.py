class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        index = 0
        while index < len(bits) - 1:
            if bits[index] == 0:
                index += 1
            else:
                index += 2
        
        return index == len(bits) - 1
