/* Write your PL/SQL query statement below */
SELECT customer_number
FROM (
    SELECT customer_number, COUNT(*) AS customer_count,
           MAX(COUNT(*)) OVER () AS max_customer_count
    FROM orders
    GROUP BY customer_number
)
WHERE customer_count = max_customer_count;


