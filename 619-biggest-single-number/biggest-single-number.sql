/* Write your PL/SQL query statement below */
SELECT MAX(num) AS num
FROM (
    SELECT num, COUNT(num) AS cnt
    FROM MyNumbers
    GROUP BY num
    HAVING COUNT(num) = 1
) subquery;
