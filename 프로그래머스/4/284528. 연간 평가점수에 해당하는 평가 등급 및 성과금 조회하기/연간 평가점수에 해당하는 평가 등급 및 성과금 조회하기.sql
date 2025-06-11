select b.EMP_NO, b.EMP_NAME as EMP_NAME, c.GRADE,
    case when c.GRADE = 'S' then b.SAL * 0.2 
        when c.GRADE = 'A' then b.SAL * 0.15
        when c.GRADE = 'B' then b.SAL * 0.1
        else 0 end as BONUS
from HR_EMPLOYEES as b
join (select 
        EMP_NO,
        case when avg(SCORE) >= 96 then 'S'
        when avg(SCORE) >= 90 then 'A'
        when avg(SCORE) >= 80 then 'B'
        else 'C' end as GRADE
    from HR_GRADE
     group by EMP_NO) as c
on b.EMP_NO = c.EMP_NO
order by b.EMP_NO;