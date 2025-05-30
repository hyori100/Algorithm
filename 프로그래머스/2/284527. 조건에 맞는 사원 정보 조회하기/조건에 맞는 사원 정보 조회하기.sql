select c.SCORE, b.EMP_NO, b.EMP_NAME, b.POSITION, b.EMAIL 
from HR_DEPARTMENT as a
join HR_EMPLOYEES as b
on a.DEPT_ID = b.DEPT_ID
join (select EMP_NO, sum(score) as SCORE from HR_GRADE group by EMP_NO order by sum(score) desc limit 1) as c
on b.EMP_NO = c.EMP_NO;