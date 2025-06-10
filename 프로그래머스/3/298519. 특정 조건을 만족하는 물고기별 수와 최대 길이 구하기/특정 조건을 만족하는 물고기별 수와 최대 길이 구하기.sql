select count(*) as FISH_COUNT, max(length) as MAX_LENGTH, FISH_TYPE from FISH_INFO
group by FISH_TYPE
having avg(case when length is not null then length else 10 end) >= 33
order by FISH_TYPE;