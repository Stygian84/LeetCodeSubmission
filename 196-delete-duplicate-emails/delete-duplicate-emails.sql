# Write your MySQL query statement below
DELETE p1
FROM person p1
LEFT JOIN (
    SELECT MIN(p2.id) AS id
    FROM person p2
    GROUP BY p2.email
) AS valid_ids ON p1.id = valid_ids.id
WHERE valid_ids.id IS NULL;
