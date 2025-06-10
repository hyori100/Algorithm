select a.ANIMAL_ID, b.NAME from ANIMAL_INS as a
join ANIMAL_OUTS as b
on a.ANIMAL_ID = b.ANIMAL_ID
order by datediff(b.DATETIME, a.DATETIME) desc
limit 2;