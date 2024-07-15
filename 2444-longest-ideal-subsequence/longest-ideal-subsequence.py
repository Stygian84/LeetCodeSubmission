class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        dp = {chr(i + ord('a')): 0 for i in range(26)}

        for char in s:
            max_length = 0
            for diff in range(-k, k + 1):
                prev_char = chr(ord(char) + diff)
                if 'a' <= prev_char <= 'z':
                    max_length = max(max_length, dp[prev_char])
            dp[char] = max_length + 1

        return max(dp.values())