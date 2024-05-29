/* Write your PL/SQL query statement below */
select TO_CHAR(activity_date, 'YYYY-MM-DD') as day, count(distinct(user_id)) as active_users
from activity
where (activity_date BETWEEN DATE '2019-06-28' AND DATE '2019-07-27') 
group by activity_date
order by day asc;