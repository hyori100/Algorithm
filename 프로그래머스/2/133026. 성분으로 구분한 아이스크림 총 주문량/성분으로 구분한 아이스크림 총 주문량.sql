-- 코드를 입력하세요
SELECT INGREDIENT_TYPE, sum(TOTAL_ORDER) as TOTAL_ORDER FROM FIRST_HALF as a
join ICECREAM_INFO as b
on a.FLAVOR = b.FLAVOR
group by b.INGREDIENT_TYPE
order by TOTAL_ORDER;