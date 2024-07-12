class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def remove_substring(s, first, second, points):
            stack = []
            total_points = 0
            for char in s:
                if stack and stack[-1] == first and char == second:
                    stack.pop()
                    total_points += points
                else:
                    stack.append(char)
            return ''.join(stack), total_points
        
        if x >= y:
            s, points1 = remove_substring(s, 'a', 'b', x)
            _, points2 = remove_substring(s, 'b', 'a', y)
        else:
            s, points1 = remove_substring(s, 'b', 'a', y)
            _, points2 = remove_substring(s, 'a', 'b', x)
        
        return points1 + points2