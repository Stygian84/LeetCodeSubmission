class Solution:
    def fractionAddition(self, expression: str) -> str:
        res="0/1"

        def gcd(a,b):
            while b:
                a,b=b,a%b
            return a

        def lcm(a,b):
            return abs(a * b) // gcd(a, b)

        def process(item,res):
            sign=1
            if item[0]=="-":
                sign=-1
            if item[0]=="+" or item[0]=="-":
                item=item[1:]
            temp_ls=item.split("/")
            a=int(temp_ls[0])*sign
            b=int(temp_ls[1])

            
            sign=1
            if res[0]=="-":
                sign=-1
            if res[0]=="+" or res[0]=="-":
                res=res[1:]
            temp_ls2=res.split("/")
            print(temp_ls2)
            c=int(temp_ls2[0])*sign
            d=int(temp_ls2[1])

            a=a*d+c*b
            b=b*d

            x=gcd(abs(a),b)

            return  str(int(a/x))+"/"+str(int(b/x))

        temp_str=""

        for item in expression:
            if item == "+" or item=="-":
                if temp_str:
                    res=process(temp_str,res)
                temp_str=""
            temp_str+=item

        res=process(temp_str,res)

        return res