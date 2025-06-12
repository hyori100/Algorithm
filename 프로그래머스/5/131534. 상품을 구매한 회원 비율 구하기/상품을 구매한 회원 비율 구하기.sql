with se as(
    select USER_ID from USER_INFO
    where year(joined) = 2021
)select year(SALES_DATE) as YEAR, month(SALES_DATE) as MONTH, 
    count(distinct b.user_id) as PURCHASED_USERS,
    round(count(distinct b.user_id)/(select count(*) from se),1) as PUCHASED_RATIO
    from se as a
    join ONLINE_SALE as b
    on a.USER_ID = b.USER_ID
    group by YEAR, MONTH
    order by YEAR, MONTH