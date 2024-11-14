class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        
        position = defaultdict(list)
        
        n = len(cards)
        res = math.inf

        for i in range(n):
            position[cards[i]].append(i)
            if len(position[cards[i]])>1:
                res = min(res, position[cards[i]][-1] - position[cards[i]][-2] + 1)
        
        if res == math.inf:
            return -1
        return res