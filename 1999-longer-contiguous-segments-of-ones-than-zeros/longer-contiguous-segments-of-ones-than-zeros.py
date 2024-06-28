class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        max_zero=0
        max_one=0

        count_zero=0
        count_one=0
        for letter in s:
            if letter=="0":
                count_one=0
                count_zero+=1
            else:
                count_one+=1
                count_zero=0
            max_zero=max(max_zero,count_zero)
            max_one=max(max_one,count_one)
        return max_one>max_zero