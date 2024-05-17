class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        def encrypt(x):
            str_x=str(x)
            return int((str(max(str_x)))*len(str_x))
        total=0
        for item in nums:
            total+=encrypt(item)
        return total