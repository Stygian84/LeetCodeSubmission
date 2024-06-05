class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        column=0
        col_res=[]
        res=[[0]*len(score[0])]*len(score)
        for i in range(len(score)):
            col_res.append(score[i][k])
        col_res.sort(reverse=True)
        for i in range(len(score)):
            for j in range(len(col_res)):
                if score[i][k]==col_res[j]:
                    res[j]=score[i]
                    break
        return res