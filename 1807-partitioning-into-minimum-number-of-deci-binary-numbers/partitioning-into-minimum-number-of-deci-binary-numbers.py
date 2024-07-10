class Solution:
    def minPartitions(self, n: str) -> int:
        max_digit="0"
        for digit in n:
            if digit>max_digit:
                max_digit=digit
                if max_digit=="9":
                    return 9
        return int(max_digit)