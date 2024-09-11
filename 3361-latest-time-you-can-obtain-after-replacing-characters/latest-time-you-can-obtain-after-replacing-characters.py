class Solution:
    def findLatestTime(self, s: str) -> str:
        
        ls = s.split(":")
        hour = ls[0]
        minute = ls[1]
        if minute=="??":
            ls[1]="59"
        elif minute[0]=="?":
            ls[1] = "5"+minute[-1]
        elif minute[1]=="?":
            ls[1] = minute[0]+"9"    
        
        if hour=="??":
            ls[0]="11"
        elif hour[0]=="?":
            if hour[1]<="1":
                ls[0] = "1"+hour[1]
            else:
                ls[0] = "0"+hour[1]
        elif hour[1]=="?":
            if hour[0]=="1":
                ls[0]="11"
            else:
                ls[0]="09"
        
        return ":".join(ls)