-- 코드를 입력하세요
SELECT a.FLAVOR from FIRST_HALF as a
join ICECREAM_INFO as b
on a.FLAVOR = b.FLAVOR and a.TOTAL_ORDER > 3000
where b.INGREDIENT_TYPE = 'fruit_based'
order by TOTAL_ORDER desc;