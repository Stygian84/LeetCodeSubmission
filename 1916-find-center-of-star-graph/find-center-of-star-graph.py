class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        first_digit=edges[0][0]
        second_digit=edges[0][1]
        if first_digit in edges[1]:
            return first_digit
        else:
            return second_digit
        