with cte as(
    select max(LENGTH) as length, FISH_TYPE from FISH_INFO 
    group by FISH_TYPE
)
select a.ID, c.FISH_NAME, a.LENGTH from FISH_INFO as a
join cte as b
on a.FISH_TYPE = b.FISH_TYPE and a.length = b.LENGTH
join FISH_NAME_INFO as c
on a.FISH_TYPE = c.FISH_TYPE
order by ID;
