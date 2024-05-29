/* Write your PL/SQL query statement below */
select e1.name,b1.bonus
from employee e1 
left join bonus b1 on b1.empId=e1.empId
where b1.bonus<1000 or b1.bonus is null;