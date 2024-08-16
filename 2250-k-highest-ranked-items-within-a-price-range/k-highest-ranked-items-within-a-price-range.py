class Solution:
    def highestRankedKItems(self, grid: List[List[int]], pricing: List[int], start: List[int], k: int) -> List[List[int]]:
        a, b = start
        res = []  # (distance, price, row, column)
        n, m = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        
        def bfs(x, y):
            nonlocal res
            queue = deque([(x, y, 0)])
            seen = set()
            seen.add((x, y))
            
            while queue:
                cx, cy, distance = queue.popleft()
                
                if pricing[0] <= grid[cx][cy] <= pricing[1]:
                    res.append((distance, grid[cx][cy], cx, cy))
                
                for dx, dy in directions:
                    nx, ny = cx + dx, cy + dy
                    if 0 <= nx < n and 0 <= ny < m and (nx, ny) not in seen and grid[nx][ny] != 0:
                        seen.add((nx, ny))
                        queue.append((nx, ny, distance + 1))
        
        bfs(a, b)
        res.sort()
        result = [[x[2], x[3]] for x in res[:k]]
        
        return result



        