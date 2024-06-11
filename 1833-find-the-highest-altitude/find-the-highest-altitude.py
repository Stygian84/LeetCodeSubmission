class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        highest=0
        step=0
        for item in gain:
            step+=item
            if step>highest:
                highest=step
        return highest