class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        def convertToMinutes(time):
            ls=time.split(":")
            res=int(ls[0])*60+int(ls[1])
            return res
        value=convertToMinutes(correct)-convertToMinutes(current)
        count=0
        while value>0:
            if value>=60:
                value-=60
                count+=1
                continue
            if value>=15:
                value-=15
                count+=1
                continue
            if value>=5:
                value-=5
                count+=1
                continue
            if value>=1:
                value-=1
                count+=1
                continue
        return count