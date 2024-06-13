class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        
        ans=[]
        all_y=[]
        base=1
        while base<bound and y!=1:
            all_y.append(base)
            base*=y
        all_x=[]
        base=1
        while base<bound and x!=1:
            all_x.append(base)
            base*=x
        if all_x==[]:
            all_x=[1]
        if all_y==[]:
            all_y=[1]

        for i in all_x:
            for j in all_y:
                if i+j<=bound:
                    if i+j not in ans:
                        ans.append(i+j)
                else:
                    break
        return ans