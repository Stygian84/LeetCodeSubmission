class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        total=sum(cardPoints)

        n=len(cardPoints)
        window=deque([])
        window_length=n-k
        window_total=0
        if window_length==0:
            return total

        min_window_total=math.inf
        for item in cardPoints:
            if len(window)==window_length:
                min_window_total=min(min_window_total,window_total)
                window_total-=window.popleft()

            if len(window)<window_length:
                window.append(item)
                window_total+=item
                
        min_window_total=min(min_window_total,window_total)
        return total-min_window_total