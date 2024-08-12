class Solution:
    def losingPlayer(self, x: int, y: int) -> str:
        
        winner = True # T,F = Alice,Bob

        while True:
            x-=1
            y-=4
            if x<0 or y<0:
                break
            winner = not winner
        
        if not winner:
            return "Alice"
        return "Bob"