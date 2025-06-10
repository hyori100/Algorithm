select * from
(select date_format(SALES_DATE, '%Y-%m-%d') as SALES_DATE, PRODUCT_ID, USER_ID, SALES_AMOUNT from ONLINE_SALE
where SALES_DATE between '2022-03-01' and '2022-03-31'
union all
select date_format(SALES_DATE, '%Y-%m-%d') as SALES_DATE, PRODUCT_ID, null as USER_ID, SALES_AMOUNT from OFFLINE_SALE 
where SALES_DATE between '2022-03-01' and '2022-03-31') as a
order by SALES_DATE, a.PRODUCT_ID, USER_ID;