-- 코드를 입력하세요
SELECT a.REST_ID, a.REST_NAME, a.FOOD_TYPE, a.FAVORITES, a.ADDRESS,
round(avg(b.REVIEW_SCORE),2) as SCORE
from REST_INFO as a
join REST_REVIEW as b
on a.REST_ID = b.REST_ID
group by REST_ID
having address like '서울%'
order by SCORE desc, a.FAVORITES desc;