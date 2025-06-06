-- 코드를 입력하세요
SELECT a.PRODUCT_ID, a.PRODUCT_NAME, (a.PRICE * SUM(b.AMOUNT)) AS TOTAL_SALES 
from FOOD_PRODUCT as a 
join FOOD_ORDER as b
on a.PRODUCT_ID = b.PRODUCT_ID and year(PRODUCE_DATE) = 2022 and month(PRODUCE_DATE) = 5 
group by PRODUCT_ID
ORDER BY TOTAL_SALES desc, a.PRODUCT_ID;