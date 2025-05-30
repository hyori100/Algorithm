-- 코드를 작성해주세요
select COUNT(*) AS FISH_COUNT, month(TIME) AS MONTH from FISH_INFO
group by month(TIME)
order by month(TIME);