with cte as(
    SELECT max(PRICE) as price, CATEGORY from FOOD_PRODUCT 
    where CATEGORY in ('과자', '국', '김치', '식용유')
    group by CATEGORY
)
select c.CATEGORY, b.price as MAX_PRICE, c.PRODUCT_NAME from FOOD_PRODUCT as c
join cte as b 
on c.CATEGORY = b.CATEGORY and c.price = b.PRICE
order by MAX_PRICE desc;