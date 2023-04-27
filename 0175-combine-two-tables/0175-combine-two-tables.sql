# Write your MySQL query statement below
SELECT 
    firstName, lastName, city, state
FROM 
    Address
Right Join
    Person
ON
    Person.personId = Address.personId