class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        
        graph = defaultdict(list)
        for (a, b), prob in zip(edges, succProb):
            graph[a].append((b, prob))
            graph[b].append((a, prob))
        
        max_heap = [(-1, start_node)]  
        max_prob = {i: 0 for i in range(n)}
        max_prob[start_node] = 1

        while max_heap:
            current_prob, current_node = heapq.heappop(max_heap)
            current_prob = -current_prob  

            if current_node == end_node:
                return current_prob
            
            for neighbor, prob in graph[current_node]:
                new_prob = current_prob * prob
                if new_prob > max_prob[neighbor]:
                    max_prob[neighbor] = new_prob
                    heapq.heappush(max_heap, (-new_prob, neighbor))

        return 0
