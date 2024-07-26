class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        INF = float('inf')
        
        dist = [[INF] * n for _ in range(n)]
        for i in range(n):
            dist[i][i] = 0
        for fromi, toi, weighti in edges:
            dist[fromi][toi] = weighti
            dist[toi][fromi] = weighti
        
        
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
                        
        minReachableCities = n
        resultCity = -1
        for i in range(n):
            count = sum(1 for j in range(n) if dist[i][j] <= distanceThreshold)
            if count < minReachableCities or (count == minReachableCities and i > resultCity):
                minReachableCities = count
                resultCity = i
                
        return resultCity