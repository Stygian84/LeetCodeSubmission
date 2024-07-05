class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        def filter(num):
            ls=num.split("+")
            real,imag=0,0
            if len(ls[0])>0:
                real=int(ls[0])
            if len(ls[1])>0:
                imag=int(ls[1][:-1])
            return real,imag

        a,b = filter(num1)
        c,d = filter(num2)

        real = str(a*c-b*d)
        imag = str(a*d+b*c)+"i"
        return real+"+"+imag