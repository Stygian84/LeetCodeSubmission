class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:

        window = []
        longest_window = 0

        for item in nums:
            longest_window = max(len(window), longest_window)

            #leftmost element
            if len(window) == 0 and item % 2 == 0 and item <= threshold:
                window.append(item)
                continue

            if window and window[-1] % 2 != item % 2 and item <= threshold:
                window.append(item)
                continue
            else:
                window = []
                #leftmost element
                if len(window) == 0 and item % 2 == 0 and item <= threshold:
                    window.append(item)
                    continue
                    
        # final check
        longest_window = max(len(window), longest_window)
        return longest_window
