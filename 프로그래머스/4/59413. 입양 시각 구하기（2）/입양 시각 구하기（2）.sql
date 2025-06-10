set @hour = -1;

select (case when hour(DATETIME) is null then b.HOUR else hour(DATETIME) end) as HOUR, 
count(hour(DATETIME)) as COUNT 
from ANIMAL_OUTS as a
right outer join (select (@hour := @hour + 1) as HOUR from ANIMAL_OUTS where @hour < 23) as b
on hour(a.DATETIME) = b.HOUR
group by HOUR
order by HOUR;