class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res=[0]*len(temperatures)
        stack=[]
        for i in range(len(temperatures)):
            item=temperatures[i]
            while stack and temperatures[stack[-1]]<item:
                prev_idx=stack.pop()
                res[prev_idx]=i-prev_idx
            stack.append(i)
        return res
        '''res=[0]*len(temperatures)
        for i in range(len(temperatures)):
            for j in range(i+1,len(temperatures)):
                if temperatures[j]>temperatures[i]:
                    res[i]=j-i
                    break
        return res'''
        