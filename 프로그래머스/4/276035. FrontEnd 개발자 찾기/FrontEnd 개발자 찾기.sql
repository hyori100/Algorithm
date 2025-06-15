with frontend as(
    select CODE from SKILLCODES where CATEGORY='Front End'
)
select distinct ID, EMAIL, FIRST_NAME, LAST_NAME from DEVELOPERS, frontend
where SKILL_CODE & CODE 
order by ID;