class Solution:
    def isNumber(self, s: str) -> bool:
        digits="0123456789"
        s=s.lower()
        if s.count("e")>1:
            return False
        if s.count(".")>1:
            return False

        ls = s.split("e")
        ls2 = []

        for item in ls:
            if item:
                ls2.append(item)
                
        if len(ls2)>2 or len(ls2)==0:
            return False

        print(ls2)

        def isDecimal(num):
            dot_count=0
            for i in range(len(num)):
                if i==0 and (num[i]=="+" or num[i]=="-"):
                    if len(num)==1:
                        return False
                    continue
                if num[i] in digits:
                    continue
                
                if num[i]==".":
                    dot_count+=1
                    if dot_count!=1:
                        return False
                    if len(num)==1:
                        return False
                    if (i!=0 and num[i-1] in digits) or (i<len(num)-1 and num[i+1] in digits):
                        continue
                    else:
                        return False
                return False

                
                

            return True
        
        def isInt(num):
            for i in range(len(num)):
                if i==0 and (num[i]=="+" or num[i]=="-"):
                    if len(num)==1:
                        return False
                    continue
                if num[i] in digits:
                    continue
                return False
            return True

        print(isDecimal(ls2[0]))
        if len(ls2)==1:
            if "e" in s:
                return False
            else:
                return isInt(ls2[0]) or isDecimal(ls2[0])
        else:
            return (isInt(ls2[0]) or isDecimal(ls2[0])) and isInt(ls2[1])
            

        '''digits="1234567890"
        isExponent=False
        for i in range(len(s)):
            print(s[i])
            if i==0 and (s[i]=="-" or s[i]=="+"):
                continue
            if i==0 and s[i]=="." and len(s)>1 and s[i+1] in digits:
                continue

            if isExponent and s[i]==".": #filter decimal after exponent
                return False


            if s[i] in digits:
                continue

            if i!=0 and (( s[i] == "." ) or (s[i]=="e") or (s[i]=="E")):

                if (s[i-1] in digits) and (s[i+1] in digits):
                    isExponent=True
                    continue
                if i>1 and s[i-1]=="." and s[i-2] in digits:
                    isExponent=True
                    continue


            if s[i]=="-" or s[i]=="+":
                return False
            
            return False
        return True 
        '''
