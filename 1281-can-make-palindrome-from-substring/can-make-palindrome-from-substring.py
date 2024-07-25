class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        
        n = len(s)
        prefix_count = [[0] * 26 for _ in range(n + 1)]
        
        for i in range(n):
            for j in range(26):
                prefix_count[i + 1][j] = prefix_count[i][j]
            prefix_count[i + 1][ord(s[i]) - ord('a')] += 1
        
        def countOdds(left: int, right: int) -> int:
            odds = 0
            for j in range(26):
                count = prefix_count[right + 1][j] - prefix_count[left][j]
                if count % 2 != 0:
                    odds += 1
            return odds
        
        res = []
        for left, right, k in queries:
            odds = countOdds(left, right)
            res.append(odds // 2 <= k)
        
        return res