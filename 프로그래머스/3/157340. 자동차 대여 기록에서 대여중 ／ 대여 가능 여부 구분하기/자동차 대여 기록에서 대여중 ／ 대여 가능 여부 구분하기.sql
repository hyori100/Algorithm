-- 코드를 입력하세요
SELECT a.CAR_ID, if(b.AVAILABILITY is null, '대여 가능', b.AVAILABILITY) as AVAILABILITY
from CAR_RENTAL_COMPANY_RENTAL_HISTORY as a
left join (
    select 
        CAR_ID, '대여중' as AVAILABILITY
    from CAR_RENTAL_COMPANY_RENTAL_HISTORY
    where ('2022-10-16' between START_DATE and END_DATE) or END_DATE = '2022-10-16') as b
on a.CAR_ID = b.CAR_ID
group by CAR_ID
order by CAR_ID desc;
