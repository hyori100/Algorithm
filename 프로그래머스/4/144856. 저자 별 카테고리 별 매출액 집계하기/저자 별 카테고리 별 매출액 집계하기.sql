-- 코드를 입력하세요
SELECT a.AUTHOR_ID, AUTHOR_NAME, CATEGORY, sum(SALES*price) as TOTAL_SALES from BOOK as a
join AUTHOR as b
on a.AUTHOR_ID = b.AUTHOR_ID
join BOOK_SALES as c
on a.BOOK_ID = c.BOOK_ID
where year(SALES_DATE) = 2022 and month(SALES_DATE) = 1
group by CATEGORY, AUTHOR_ID
order by AUTHOR_ID, CATEGORY desc;