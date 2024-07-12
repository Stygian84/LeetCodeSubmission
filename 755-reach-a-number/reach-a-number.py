class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        numMoves = 0
        currentSum = 0
        
        while currentSum < target or (currentSum - target) % 2 != 0:
            numMoves += 1
            currentSum += numMoves
        
        return numMoves