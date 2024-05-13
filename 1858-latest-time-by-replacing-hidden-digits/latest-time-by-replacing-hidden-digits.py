class Solution:
    def maximumTime(self, time: str) -> str:
        hour=True
        ls=[1]*5
        for i in range(len(time)):
            print(time[i],i)
            if time[i]=="?":
                if i==1 or i==4:
                    if ls[0]=="2" and i==1:
                        ls[i]="3"
                    else:
                        ls[i]="9"
                if i==0:
                    ls[i]="2"
                if i==3:
                    ls[i]="5"
                    print("a",ls)
            else:
                ls[i]=str(time[i])
        print(ls)
        if int(ls[1])>=4 and time[0]=="?":
            ls[0]="1"
        return "".join(ls)


        