class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        alice = []
        bob = []
        for day in days:
            alice.append([False]*day)
        for day in days:
            bob.append([False]*day)
        

        def parse(x):
            day = int(x[3:])-1
            month = int(x[:2])-1
            return [day,month]

        def fill(d1,m1,d2,m2,arr):
            if m1==m2: #same month
                for i in range(d1,d2+1):
                    arr[m1][i]=True
                return arr
            elif m2>m1: #different month

                for month in range(m1,m2+1):
                    n = days[month]
                    if month==m2:
                        for j in range(d2+1):
                            arr[month][j]=True
                    elif month == m1:
                        for j in range(d1,n):
                            arr[month][j]=True
                    else:
                        for j in range(n):
                            arr[month][j] = True
            else: #different month

                for month in range(m1,12):
                    n = days[month]
                    
                    if month == m1:
                        for j in range(d1,n):
                            arr[month][j]=True
                    else:
                        for j in range(n):
                            arr[month][j] = True

                for month in range(m2+1):
                    n = days[month]
                    if month==m2:
                        for j in range(d2+1):
                            arr[month][j]=True
                    else:
                        for j in range(n):
                            arr[month][j] = True
            return arr

        #Alice
        d1,m1 = parse(arriveAlice)
        d2,m2 = parse(leaveAlice)

        alice = fill(d1,m1,d2,m2,alice)
        
        #Bob
        d3,m3 = parse(arriveBob)
        d4,m4 = parse(leaveBob)

        bob = fill(d3,m3,d4,m4,bob)

        count = 0
        start = min(m1,m3)
        end = max(m2,m4)
        for i in range(start,end+1):
            n = days[i]
            if i == 7:
                print(alice[i],bob[i],i)
            for j in range(n):
                if alice[i][j]==True and bob[i][j]==True:
                    count+=1

        return count