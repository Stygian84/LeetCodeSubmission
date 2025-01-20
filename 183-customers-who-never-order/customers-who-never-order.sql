# Write your MySQL query statement below
select c1.name as customers from customers c1 left join orders o1 on c1.id = o1.customerId where o1.id is null