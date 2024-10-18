class Solution:
    def rotatedDigits(self, n: int) -> int:
        #invalid = 3,4,7
        # 0 = 0
        # 1 = 1
        # 8 = 8
        # 2 = 5
        # 5 = 2
        # 6 = 9
        # 9 = 6
        invalid = set({"3","4","7"})
        half_valid = set({"0","1","8"})

        def isValid(x):
            str_x = str(x)
            flag = False #True if at least 1 non-zero or non-one or non-8
            for digit in str_x:
                if digit in invalid:
                    return False
                if digit not in half_valid:
                    flag = True
            return flag            

        
        count = 0
        for num in range(2,n+1):
            if isValid(num):
                count+=1
        return count