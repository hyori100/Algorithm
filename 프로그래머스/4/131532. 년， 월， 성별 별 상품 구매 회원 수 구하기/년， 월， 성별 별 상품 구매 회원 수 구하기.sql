-- 코드를 입력하세요
SELECT 
    year(SALES_DATE) as YEAR, 
    MONTH(SALES_DATE) as MONTH, 
    GENDER,
    count(distinct a.USER_ID) as USERS
from USER_INFO as a
join ONLINE_SALE as b
on a.USER_ID = b.USER_ID
where GENDER is not null
group by year(SALES_DATE), MONTH(SALES_DATE), GENDER
order by YEAR, MONTH, GENDER