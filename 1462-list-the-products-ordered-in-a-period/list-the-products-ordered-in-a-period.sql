# Write your MySQL query statement below
select p.product_name, sum(t.unit) as unit
from products p
join (select * from orders where order_date BETWEEN '2020-02-01' AND '2020-02-29') as t
on p.product_id=t.product_id
group by p.product_id
having sum(t.unit)>=100

