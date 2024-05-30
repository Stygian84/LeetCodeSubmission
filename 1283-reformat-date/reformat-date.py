class Solution:
    def reformatDate(self, date: str) -> str:
        days = ["1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th", "9th", "10th",
        "11th", "12th", "13th", "14th", "15th", "16th", "17th", "18th", "19th", "20th",
        "21st", "22nd", "23rd", "24th", "25th", "26th", "27th", "28th", "29th", "30th", "31st"]

        month=["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        
        ls=date.split()

        ls[0]=str(days.index(ls[0])+1).zfill(2)
        ls[1]=str(month.index(ls[1])+1).zfill(2)
        ls.reverse()
        return "-".join(ls)
        