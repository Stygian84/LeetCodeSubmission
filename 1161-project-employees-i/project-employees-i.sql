/* Write your PL/SQL query statement below */
select p.project_id, ROUND(AVG(e.experience_years), 2) as average_years
from project p
join employee e on e.employee_id=p.employee_id
group by p.project_id
order by p.project_id asc
