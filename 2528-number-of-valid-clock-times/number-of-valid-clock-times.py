class Solution:
    def countTime(self, time: str) -> int:
        hour,minute = time.split(":")
        count = 1
        if hour[0]=="?":
            if hour[1]=="?":
                count=24
            else:
                if hour[1]>="4":
                    count=2
                else:
                    count=3
        else:
            if hour[1]=="?":
                if hour[0]=="2":
                    count=4
                else:
                    count=10
            else:
                count=1

        count2 = 1
        if minute[0]=="?":
            if minute[1]=="?":
                count2=60
            else:
                count2=6
        else:
            if minute[1]=="?":
                count2=10
            else:
                count2=1
        
        return count*count2
        