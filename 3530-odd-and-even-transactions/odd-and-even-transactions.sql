# Write your MySQL query statement below
select t1.transaction_date , 
    SUM(CASE WHEN t1.amount % 2 = 1 THEN t1.amount ELSE 0 END) AS odd_sum,
    SUM(CASE WHEN t1.amount % 2 = 0 THEN t1.amount ELSE 0 END) AS even_sum
from transactions t1
join transactions t2
on t1.transaction_id=t2.transaction_id
group by t1.transaction_date
order by t1.transaction_date asc