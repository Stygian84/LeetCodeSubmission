class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        h=0
        for idx in range(len(citations)):
            if citations[idx]>=idx+1:
                h=idx+1
            else:
                break
        return h
        