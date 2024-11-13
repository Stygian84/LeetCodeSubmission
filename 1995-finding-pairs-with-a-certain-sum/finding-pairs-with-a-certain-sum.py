class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.freq = Counter(nums2)

    def add(self, index: int, val: int) -> None:
        self.freq[self.nums2[index]]-=1
        self.nums2[index]+=val
        self.freq[self.nums2[index]]+=1

    def count(self, tot: int) -> int:
        res = 0

        for i in range(len(self.nums1)):
            diff = tot-self.nums1[i]
            if diff in self.freq:
                res += self.freq[diff]
        return res

# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)