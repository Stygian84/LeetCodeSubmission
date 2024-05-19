class Solution:
    def dayOfYear(self, date: str) -> int:
        year=date[:4]
        month=date[5:7]
        day=date[-2:]
        leap_year=False
        if (int(year)%4==0 and int(year)%100!=0 )or int(year)%400==0:
            leap_year=True
        total=0
        for i in range(1,int(month)):
            if i<=7:
                if i%2==1:
                    total+=31
                elif i==2:
                    if leap_year:
                        total+=29
                    else:
                        total+=28
                else:
                    total+=30
            elif i>7:
                if i%2==1:
                    total+=30
                else:
                    total+=31
        
        return total+int(day)