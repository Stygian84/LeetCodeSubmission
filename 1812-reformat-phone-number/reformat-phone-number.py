class Solution:
    def reformatNumber(self, number: str) -> str:
        number=number.replace(" ","").replace("-","")
        print(number)
        count=0
        result=[]
        for i in range(len(number)):
            if i%3==0 and i!=0:
                result.append("-")
            result.append(number[i])

        print(result)
        if result[-2]=="-":
            result[-2],result[-3]=result[-3],result[-2]
        
        return "".join(result)

        