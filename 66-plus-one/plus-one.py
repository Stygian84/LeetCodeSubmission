class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num=""
        for item in digits:
            num+=str(item)
        print(num)
        num=int(num)
        num+=1
        result=[]
        for item in str(num):
            result.append(int(item))
        return result