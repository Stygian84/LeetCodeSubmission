class Solution:
    def numSquares(self, n: int) -> int:
        
        squares = []
        for i in range(1,int(n**0.5)+1):
            squares.append(i*i)
        
        queue = deque([n])
        level = 0

        while queue:
            level += 1
            for _ in range(len(queue)):
                remainder = queue.popleft()

                for square in squares:
                    if remainder == square:
                        return level
                    if remainder<square:
                        break
                    queue.append(remainder-square)
                    
        return level
