class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        result=[0]*len(code)
        code_2=code*2
        if k==0:
            return result
        elif k>0:
            for i in range(len(code)):
                result[i] = sum(code_2[i+1:i+1+k])
            return result
        else:
            for i in range(len(code),len(code_2)):
                result[i-len(code)] = sum(code_2[i+k:i])
            return result
        