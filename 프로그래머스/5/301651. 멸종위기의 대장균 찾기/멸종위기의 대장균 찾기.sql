with recursive tmp as(
    select ID, PARENT_ID,  1 as generation
    from ECOLI_DATA 
    where PARENT_ID is null
    union all
    select b.id, b.PARENT_ID, tmp.generation + 1 as generation
    from tmp
    join ECOLI_DATA as b 
    on tmp.Id = b.PARENT_ID
)
select count(id) as COUNT, GENERATION from tmp
where id not in (select distinct parent_id from tmp where parent_id is not null)
group by GENERATION;