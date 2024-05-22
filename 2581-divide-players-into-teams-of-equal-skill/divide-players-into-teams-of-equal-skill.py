class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        current=skill[0]+skill[-1]
        ls=[]
        for i in range(len(skill)//2):
            if skill[i]+skill[-(i+1)]!=current:
                return -1
            else:
                ls.append(skill[i]*skill[-(i+1)])
        return sum(ls)