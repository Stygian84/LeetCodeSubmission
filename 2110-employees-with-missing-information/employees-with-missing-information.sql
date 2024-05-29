/* Write your PL/SQL query statement below */
select COALESCE(e.employee_id, s.employee_id) as employee_id
from employees e
right join salaries s on e.employee_id = s.employee_id
where e.name is null
union
select COALESCE(e.employee_id, s.employee_id) as employee_id
from employees e
left join salaries s on e.employee_id = s.employee_id
where s.salary is null;

