class Solution:
    def splitIntoFibonacci(self, num: str) -> List[int]:
        
        res = []
        n = len(num)
        def backtrack(start,path):
            nonlocal res
            if start==n and len(path)>2:
                res = path[:]
                return
            if res:
                return
            
            for i in range(start,n+1):
                str_num = num[start:i+1]
                
                if not str_num:
                    continue
                if str_num[0]=="0" and len(str_num)>1:
                    break
                number = int(str_num)
                
                if number>=2**31:
                    break

                if len(path)>=2 and path[-1]+path[-2]==number:
                    path.append(number)
                    backtrack(i+1,path)
                    path.pop()
                elif len(path)<2:
                    path.append(number) 
                    backtrack(i+1,path)
                    path.pop()

        backtrack(0,[])
        return res