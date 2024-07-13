class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        robots = sorted(zip(positions, healths, directions, range(len(positions))), key=lambda x: x[0])
        
        stack = []
        survivors = {}
        
        for pos, health, dir, original_index in robots:
            if dir == 'R':
                stack.append((pos, health, dir, original_index))
            else: 
                while stack and stack[-1][2] == 'R':
                    right_pos, right_health, right_dir, right_index = stack.pop()
                    if right_health > health:
                        right_health -= 1
                        stack.append((right_pos, right_health, right_dir, right_index))
                        health = 0
                        break
                    elif right_health < health:
                        health -= 1
                    else:
                        health = 0
                        break
                if health > 0:
                    stack.append((pos, health, dir, original_index))
        
        while stack:
            pos, health, dir, original_index = stack.pop(0)
            survivors[original_index] = health
        
        result = [survivors[i] for i in range(len(positions)) if i in survivors]
        
        return result