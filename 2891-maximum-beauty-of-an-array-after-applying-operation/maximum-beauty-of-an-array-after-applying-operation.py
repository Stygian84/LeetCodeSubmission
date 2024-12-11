class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()

        print(nums)
        res = 1
        window = deque([])

        for num in nums:
            if not window:
                window.append(num)
            else:
                if num-window[0]<=k*2:
                    window.append(num)
                else:
                    res = max(len(window),res)
                    while window and num-window[0]>k*2:
                        window.popleft()
                    window.append(num)
            #print(window)
        res = max(len(window),res)

        return res