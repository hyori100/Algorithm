with cte as(
    select max(FAVORITES) as FAVORITES, FOOD_TYPE from REST_INFO 
    group by FOOD_TYPE
)
select a.FOOD_TYPE, a.REST_ID, a.REST_NAME, a.FAVORITES from REST_INFO as a
join cte as b
on a.FOOD_TYPE = b.FOOD_TYPE and a.FAVORITES = b.FAVORITES
order by FOOD_TYPE desc;
