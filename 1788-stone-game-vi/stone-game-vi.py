class Solution:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        n = len(aliceValues)
        stones = [(aliceValues[i], bobValues[i]) for i in range(n)]
        
        stones.sort(key=lambda x: x[0] + x[1], reverse=True)
        
        alice_points = 0
        bob_points = 0
        
        for i in range(n):
            if i % 2 == 0:
                alice_points += stones[i][0] 
            else:
                bob_points += stones[i][1] 
        
        if alice_points > bob_points:
            return 1
        elif alice_points < bob_points:
            return -1
        else:
            return 0