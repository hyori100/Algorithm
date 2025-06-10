select round(avg(case when LENGTH is not null then LENGTH else 10 end),2) as AVERAGE_LENGTH
from FISH_INFO


