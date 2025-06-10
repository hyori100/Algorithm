select b.YEAR, b.maxcolony - SIZE_OF_COLONY as YEAR_DEV, ID from ECOLI_DATA as a 
join (select year(DIFFERENTIATION_DATE) as YEAR, MAX(SIZE_OF_COLONY) as maxcolony
      from ECOLI_DATA
     group by YEAR) as b
on YEAR(a.DIFFERENTIATION_DATE) = b.YEAR
order by YEAR, YEAR_DEV;
