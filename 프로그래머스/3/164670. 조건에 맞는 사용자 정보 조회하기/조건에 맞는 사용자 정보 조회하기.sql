-- 코드를 입력하세요
SELECT USER_ID, NICKNAME, concat(CITY, ' ', STREET_ADDRESS1, ' ', STREET_ADDRESS2) as 전체주소, concat(substring(tlno, 1,3), '-', substring(tlno, 4,4), '-', substring(tlno, 8,4)) as 전화번호
from USED_GOODS_BOARD as a
join USED_GOODS_USER as b
on a.WRITER_ID = b.USER_ID
group by WRITER_ID
having count(WRITER_ID) >= 3
order by USER_ID desc;