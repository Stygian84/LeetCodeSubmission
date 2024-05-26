class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        max_number = ""
    
        for i in range(len(number)):
            if number[i] == digit:
                new_number = number[:i] + number[i+1:]
                if new_number > max_number:
                    max_number = new_number
        
        return max_number
        