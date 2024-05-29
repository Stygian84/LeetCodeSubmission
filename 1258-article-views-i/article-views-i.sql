/* Write your PL/SQL query statement below */
select distinct author_id as id
from views v1
where v1.author_id=v1.viewer_id
order by id asc
