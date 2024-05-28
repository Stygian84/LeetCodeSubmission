/* Write your PL/SQL query statement below */
select Person.firstName,Person.lastName,Address.city,Address.state
from Person
LEFT join Address on Person.personId=Address.personId