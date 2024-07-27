class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        cost_matrix = [[math.inf] * 26 for _ in range(26)]
        for i in range(26):
            cost_matrix[i][i] = 0
        
        for o, c, z in zip(original, changed, cost):
            o_idx = ord(o) - ord('a')
            c_idx = ord(c) - ord('a')
            cost_matrix[o_idx][c_idx] = min(cost_matrix[o_idx][c_idx], z)
        
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    if cost_matrix[i][k] < inf and cost_matrix[k][j] < inf:
                        cost_matrix[i][j] = min(cost_matrix[i][j], cost_matrix[i][k] + cost_matrix[k][j])
        
        total_cost = 0
        n = len(source)
        
        for i in range(n):
            s_char = source[i]
            t_char = target[i]
            if s_char == t_char:
                continue
            s_idx = ord(s_char) - ord('a')
            t_idx = ord(t_char) - ord('a')
            if cost_matrix[s_idx][t_idx] == inf:
                return -1
            total_cost += cost_matrix[s_idx][t_idx]
        
        return total_cost