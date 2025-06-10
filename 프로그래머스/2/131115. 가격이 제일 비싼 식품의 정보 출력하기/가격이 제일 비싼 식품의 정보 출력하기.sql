-- 코드를 입력하세요
select * from FOOD_PRODUCT
where price = (SELECT max(price) from FOOD_PRODUCT);