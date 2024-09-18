class Solution:
    def smallestNumber(self, num: int) -> int:
        if -10<=num<=10 :
            return num
        
        sign = 1
        if num<0:
            sign = -1
        
        zero = 0
        non_zero = []
        for digit in str(num):
            if digit=="-":
                continue
            if digit=="0":
                zero+=1
            else:
                non_zero.append(digit)
        
        
        if sign==1:
            non_zero.sort()
            res = [non_zero[0]] + ["0"]*zero + non_zero[1:]
        else:
            non_zero.sort(reverse=True)
            res = ["-"] + non_zero + ["0"]*zero 
        

        return int("".join(res))