with cte as(
    select 
        a.DAILY_FEE,
        a.CAR_TYPE,
        datediff(end_date, start_date)+1 as duration,
        (case 
            when datediff(end_date, start_date)+1 >= 90 then '90일 이상'
            when datediff(end_date, start_date)+1 >= 30 then '30일 이상'
            when datediff(end_date, start_date)+1 >= 7 then '7일 이상' 
            else ''
            end) as dateType, 
        a.CAR_ID, b.HISTORY_ID
    from CAR_RENTAL_COMPANY_CAR as a
    join CAR_RENTAL_COMPANY_RENTAL_HISTORY as b
    on a.CAR_ID = b.CAR_ID and a.CAR_TYPE = '트럭'
) 
select HISTORY_ID, round(DAILY_FEE * (1-ifnull(DISCOUNT_RATE, 0)*0.01) * duration) as FEE 
from cte as a
left join CAR_RENTAL_COMPANY_DISCOUNT_PLAN as b
on b.CAR_TYPE = a.CAR_TYPE and a.dateType = b.DURATION_TYPE
order by FEE desc, HISTORY_ID desc;

