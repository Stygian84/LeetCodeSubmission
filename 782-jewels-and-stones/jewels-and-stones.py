class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        result=0
        for item in jewels:
            result+=stones.count(item)
        return result