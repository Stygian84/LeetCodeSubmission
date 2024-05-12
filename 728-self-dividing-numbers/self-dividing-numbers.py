class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result=[]
        for i in range(left,right+1):
            flag=True
            for digit in str(i):
                if digit=="0":
                    flag=False
                    break
                if i%int(digit)==0:
                    continue
                else:
                    flag=False
                    break
            if flag:
                result.append(i)
        return result
            
        