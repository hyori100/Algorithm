-- 코드를 작성해주세요
select distinct ID, EMAIL, FIRST_NAME, LAST_NAME 
From SKILLCODES a, DEVELOPERS b
where a.NAME IN ('C#', 'Python')
and (a.CODE & b.SKILL_CODE) > 0
ORDER BY b.ID;