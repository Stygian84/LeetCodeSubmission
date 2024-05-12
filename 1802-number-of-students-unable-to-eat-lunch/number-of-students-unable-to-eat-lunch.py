class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        limit=0
        max_limit=len(students)+1
        if students==sandwiches:
            return 0
        while limit<max_limit:
            max_limit=len(students)+1
            if students==[]:
                return 0
            if students[0]==sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                limit=0
            else:
                limit+=1
                students=students[1:]+[students[0]]
            print(students , sandwiches , limit , max_limit)
        
        
        return len(students)
