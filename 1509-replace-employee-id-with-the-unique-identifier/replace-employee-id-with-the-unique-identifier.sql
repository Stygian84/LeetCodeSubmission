/* Write your PL/SQL query statement below */
select unique_id,name
from employees e
left join employeeuni u on e.id=u.id
