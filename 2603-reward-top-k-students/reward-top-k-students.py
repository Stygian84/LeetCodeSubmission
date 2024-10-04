class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
        
        positive = set(positive_feedback)
        negative = set(negative_feedback)
        
        scores = []
        for student,r in zip(student_id,report):
            sentence = r.split()
            points = 0
            for word in sentence:
                if word in positive:
                    points+=3
                elif word in negative:
                    points-=1
            
            scores.append((points,student))
        scores.sort(key=lambda x:(-x[0],x[1]))

        res = []
        for _,student in scores:
            res.append(student)
            k-=1
            if k==0:
                break
        return res