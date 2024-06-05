class Solution:
    def intToRoman(self, num: int) -> str:
        '''my_dict={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        reversed_dict = {key: my_dict[key] for key in reversed(my_dict)}
        freq={}
        counter=0
        value=0
        previous_key = None
        previous_value=0
        
        for key,values in reversed_dict.items():
            modifier=0
            if counter%2==0:
                modifier=5
            else:
                modifier=2
            if previous_key!=None:
                value=previous_value*modifier
            freq[key]=int(num/values)
            previous_value=freq[key]
            freq[key]-=value
            previous_key=key
            counter+=1
            print(freq,previous_key)
        print(freq)'''
        res=[]
        count=1
        one="I"
        five="V"
        ten="X"
        for item in str(num)[::-1]:
            digit=int(item)
            if count==2:
                one="X"
                five="L"
                ten="C"
            
            if count==3:
                one="C"
                five="D"
                ten="M"
            if count==4:
                one="M"
            if digit<4:
                res.append(one*digit)
            elif digit==4:
                res.append(one+five)
            elif digit<9:
                res.append(five+one*(digit-5))
            elif digit==9:
                res.append(one+ten)
            count+=1
        res.reverse()
        return "".join(res)
        