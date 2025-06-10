select concat('/home/grep/src/', a.BOARD_ID, '/', FILE_ID,FILE_NAME, FILE_EXT) FILE_PATH
from USED_GOODS_BOARD as a
join USED_GOODS_FILE as b
on a.BOARD_ID = b.BOARD_ID
where views = (
select max(VIEWS) from USED_GOODS_BOARD as a
join USED_GOODS_FILE as b
on a.BOARD_ID = b.BOARD_ID)
order by FILE_PATH desc;