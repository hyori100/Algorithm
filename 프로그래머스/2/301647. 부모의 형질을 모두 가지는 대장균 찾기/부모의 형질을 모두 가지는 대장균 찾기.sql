-- 코드를 작성해주세요
select b.ID, b.GENOTYPE, a.GENOTYPE as PARENT_GENOTYPE 
from ECOLI_DATA as a
join ECOLI_DATA as b
on a.ID = b.PARENT_ID
where a.GENOTYPE & b.GENOTYPE = a.GENOTYPE
order by b.ID;