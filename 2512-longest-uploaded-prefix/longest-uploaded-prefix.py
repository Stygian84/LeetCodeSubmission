class LUPrefix:

    def __init__(self, n: int):
        self.uploaded = [False] * (n+1)
        self.n = n
        self.prev_longest = 0

    def upload(self, video: int) -> None:
        self.uploaded[video] = True

    def longest(self) -> int:
        longest_prefix_length = self.prev_longest
        for i in range(longest_prefix_length + 1, self.n + 1):
            if self.uploaded[i]:
                longest_prefix_length = i
            else:
                break
        self.prev_longest = longest_prefix_length
        return longest_prefix_length


# Your LUPrefix object will be instantiated and called as such:
# obj = LUPrefix(n)
# obj.upload(video)
# param_2 = obj.longest()