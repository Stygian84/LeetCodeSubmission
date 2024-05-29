/* Write your PL/SQL query statement below */
select u.name,sum(t.amount) as balance
from users u
join transactions t on t.account=u.account
group by u.name
having sum(t.amount) > 10000