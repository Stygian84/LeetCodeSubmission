/* Write your PL/SQL query statement below */
SELECT email
FROM person
GROUP BY email
HAVING COUNT(email) > 1;
