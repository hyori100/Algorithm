-- 코드를 작성해주세요
select a.ID, if(b.PARENT_ID is null, 0, count(*)) as CHILD_COUNT 
from ECOLI_DATA as a
left join ECOLI_DATA as b
on a.ID = b.PARENT_ID
group by a.ID;
