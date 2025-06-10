select a.ID from ECOLI_DATA as a
join ECOLI_DATA as b
on a.PARENT_ID = b.Id
join ECOLI_DATA as c
on b.PARENT_ID = c.Id
where a.ID not in (
    select a.ID from ECOLI_DATA as a
    join ECOLI_DATA as b
    on a.PARENT_ID = b.Id
    join ECOLI_DATA as c
    on b.PARENT_ID = c.Id
    join ECOLI_DATA as d
    on c.PARENT_ID = d.Id   
)
order by a.Id;
