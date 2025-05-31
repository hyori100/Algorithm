-- 코드를 입력하세요
SELECT CATEGORY, sum(SALES) as TOTAL_SALES from BOOK as a 
join BOOK_SALES as b
on a.BOOK_ID = b.BOOK_ID
where year(SALES_DATE) = 2022 and month(SALES_DATE) = 1
group by CATEGORY
order by CATEGORY;