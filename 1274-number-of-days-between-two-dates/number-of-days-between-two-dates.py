class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        def is_leap_year(year):
            return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

        def f(date): 
            year = int(date[:4])
            month = int(date[5:7])
            day = int(date[-2:])
            
            days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            
            
            total_days = 0
            
            for y in range(1971, year):
                if is_leap_year(y):
                    total_days += 366
                else:
                    total_days += 365
                    
            for m in range(1, month):
                if m == 2 and is_leap_year(year):  
                    total_days += 29
                else:
                    total_days += days_in_month[m - 1]
            
            total_days += day
            
            return total_days

        
        return abs(f(date1)-f(date2))