class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        
        def calcScore(arr):
            total = 0
            multiplier = 1
            for i in range(len(arr)):
                if i>=1 and arr[i-1] == 10:
                        multiplier=2
                elif i>=2 and arr[i-2] == 10:
                        multiplier=2
                total += arr[i] * multiplier
                multiplier=1
            return total

        a,b = calcScore(player1),calcScore(player2)
        if a>b: return 1
        if a<b: return 2
        if a==b: return 0