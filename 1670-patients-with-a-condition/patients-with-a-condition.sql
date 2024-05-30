/* Write your PL/SQL query statement below */
SELECT *
FROM patients
WHERE conditions LIKE 'DIAB1%' OR conditions LIKE '% DIAB1%';
