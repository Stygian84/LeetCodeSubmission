class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:

        def isValid(number):
            count=defaultdict(int)
            num_str=str(number)
            
            for digit in digits:
                count[int(digit)]+=1

            for digit in num_str:
                if int(digit) not in digits:
                    return False
                count[int(digit)]-=1
                if count[int(digit)]<0:
                    return False

            return True

        res=[]
        for num in range(100,1000):
            if num%2 == 0 and isValid(num):
                res.append(num)
        return res