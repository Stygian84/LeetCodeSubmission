class Solution:
    def minPartitions(self, n: str) -> int:
        return int(sorted(list(n))[-1])