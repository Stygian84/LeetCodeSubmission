class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        attempts=minutesToTest//minutesToDie

        for i in range(buckets):
            if (attempts+1)**i>=buckets:
                return i
    