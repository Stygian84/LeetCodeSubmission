class Solution:
    def minPartitions(self, n: str) -> int:
        if '9' in n:
            return 9
        return int(max(n))