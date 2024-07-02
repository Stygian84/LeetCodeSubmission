class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        days=["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        if month==1 or month==2:
            year-=1
            month+=12
        year_of_century = year % 100
        century = year // 100
        decade = month
        weekday = (day + (13 * (decade + 1) // 5) + year_of_century + (year_of_century // 4) + (century // 4) - (2 * century)) % 7
        
        return days[weekday-1]