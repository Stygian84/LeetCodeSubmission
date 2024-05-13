class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        progress=0
        max_alt=0
        for idx in range(len(gain)):
            progress+=gain[idx]
            if progress>max_alt:
                max_alt=progress
        return max_alt
        