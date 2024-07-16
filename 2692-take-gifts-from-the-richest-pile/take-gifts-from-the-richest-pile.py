class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:

        pile = [-gift for gift in gifts]

        heapq.heapify(pile)

        for _ in range(k):
            val = -heapq.heappop(pile)
            heapq.heappush(pile,-math.floor(val**0.5))

        return -sum(pile)