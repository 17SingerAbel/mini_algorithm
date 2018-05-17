# Write your MySQL query statement below
SELECT e1.Id, e1.Month, sum(e2.Salary) as Salary
FROM Employee e1 JOIN Employee e2 on e1.Id = e2.Id and e1.Month >= e2.Month and e1.Month - e2.Month <= 2
WHERE e1.Month < (SELECT max(Month) FROM Employee where Id = e1.Id)
GROUP BY e1.Id, e1.Month
ORDER BY e1.Id ASC, e1.Month DESC