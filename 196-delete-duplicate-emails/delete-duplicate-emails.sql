/* Write your PL/SQL query statement below */
DELETE FROM person p1
WHERE EXISTS (
    SELECT 1
    FROM person p2
    WHERE p1.email = p2.email
    AND p1.id > p2.id
);
