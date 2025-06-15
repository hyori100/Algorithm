with frontend as(
    select sum(CODE) as sumSkillCode
    from SKILLCODES 
    where CATEGORY = 'Front End'
), 
grading as(
select case 
        when (a.SKILL_CODE & b.sumSkillCode) && (a.SKILL_CODE & (select CODE from SKILLCODES where NAME='Python')) then 'A'
        when (a.SKILL_CODE & (select CODE from SKILLCODES where NAME='C#')) then 'B'
        when (a.SKILL_CODE & b.sumSkillCode) then 'C'
        else null end as Grade, ID, EMAIL
from DEVELOPERS as a
join frontend as b)
select * from grading
where Grade is not null
order by GRADE,ID;
