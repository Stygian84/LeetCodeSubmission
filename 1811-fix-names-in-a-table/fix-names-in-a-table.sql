/* Write your PL/SQL query statement below */
select user_id,INITCAP(SUBSTR(name, 1, 1)) ||
  LOWER(SUBSTR(name, 2)) as name
from users
order by user_id asc