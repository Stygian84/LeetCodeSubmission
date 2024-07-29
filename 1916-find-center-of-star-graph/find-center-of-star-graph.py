class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        if edges[0][1] == edges[1][0] or edges[0][1] == edges[1][1]:
            return edges[0][1]
        else:
            return edges[0][0]
        '''first_digit=edges[0][0]
        second_digit=edges[0][1]
        if first_digit in edges[1]:
            return first_digit
        else:
            return second_digit'''
        