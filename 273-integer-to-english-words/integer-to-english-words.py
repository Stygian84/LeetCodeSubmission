class Solution:
    def numberToWords(self, num: int) -> str:
        if num==0:
            return "Zero"

        dc = {0: "Zero",
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine",
        10: "Ten",
        11: "Eleven",
        12: "Twelve",
        13: "Thirteen",
        14: "Fourteen",
        15: "Fifteen",
        16: "Sixteen",
        17: "Seventeen",
        18: "Eighteen",
        19: "Nineteen",
        20: "Twenty",
        30: "Thirty",
        40: "Forty",
        50: "Fifty",
        60: "Sixty",
        70: "Seventy",
        80: "Eighty",
        90: "Ninety",
        100: "Hundred",
        1000: "Thousand",
        1000000: "Million",
        1000000000: "Billion"
        }
        str_num=str(num)[::-1]
        
        def parse(nums):
            
            res=[]
            for i in range(len(nums)):
                value=int(nums[i])
                if value==0:
                    continue
                #for tens
                if i==1:
                    #for 11,12...19
                    if value*10+int(nums[i-1]) in dc:
                        if int(nums[i-1])!=0:
                            res.pop()
                        res.append(dc[value*10+int(nums[i-1])])
                        continue
                    #for 20,30...,90
                    if value*(10**i) in dc:
                        res.append(dc[value*(10**i)])
                        continue
                #for hundred
                if i==2:
                    res.append("Hundred")

                #for 1,2,..,9
                res.append(dc[value])
                
            return res
        
        ls=[]
        count=0 #for thousand etc
        for i in range(0,len(str_num),3):
            temp_ls=parse(list(str_num[i:i+3]))[::-1]

            if temp_ls and count>0 and 10**(count*3) in dc: # for million thousand etc
                ls.append(dc[10**(count*3)])
            if temp_ls:
                ls.append(" ".join(temp_ls))
            count+=1

        ls.reverse()
        return " ".join(ls)