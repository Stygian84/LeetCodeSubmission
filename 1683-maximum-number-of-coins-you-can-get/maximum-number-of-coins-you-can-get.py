class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        queue=deque(piles)

        total=0
        while queue:
            queue.pop()
            total+=queue.pop()
            queue.popleft()

        return total