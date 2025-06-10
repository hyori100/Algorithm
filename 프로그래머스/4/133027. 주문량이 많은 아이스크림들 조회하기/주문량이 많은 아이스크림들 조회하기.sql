select a.FLAVOR from FIRST_HALF  as a 
join JULY as b
on a.FLAVOR = b.FLAVOR
group by a.FLAVOR
order by SUM(a.TOTAL_ORDER)+sum(b.TOTAL_ORDER) desc
limit 3;