select s1.student_id, s1.subject, s1.score as first_score, s2.score as latest_score
from scores s1 
join scores s2 on s1.student_id=s2.student_id and s1.subject=s2.subject 
and s2.exam_date = (select max(exam_date) from scores where student_id = s1.student_id and subject = s1.subject)
and s1.exam_date = (select min(exam_date) from scores where student_id = s1.student_id and subject = s1.subject)
where s2.score>s1.score
order by s1.student_id asc, s1.subject asc
