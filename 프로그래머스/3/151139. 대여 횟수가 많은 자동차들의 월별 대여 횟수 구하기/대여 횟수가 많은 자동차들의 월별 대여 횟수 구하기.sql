-- 코드를 입력하세요
SELECT month(START_DATE) as MONTH, CAR_ID, count(CAR_ID) AS RECORDS from CAR_RENTAL_COMPANY_RENTAL_HISTORY as a
 where date_format(START_DATE,'%Y-%m') between '2022-08' and '2022-10'
and car_id in (
    select car_id 
    from CAR_RENTAL_COMPANY_RENTAL_HISTORY
    where date_format(START_DATE,'%Y-%m') between '2022-08' and '2022-10'
    group by car_id 
    having count(car_id) >= 5
)
group by MONTH, CAR_ID
having RECORDS >= 1
order by MONTH, CAR_ID desc;