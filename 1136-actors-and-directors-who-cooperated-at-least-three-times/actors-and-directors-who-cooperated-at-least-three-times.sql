/* Write your PL/SQL query statement below */
select actor_id,director_id
from actordirector 
having count(1)>=3
group by actor_id,director_id