-- 코드를 작성해주세요
select b.ITEM_ID, c.ITEM_NAME, c.RARITY 
from ITEM_INFO as a
join ITEM_TREE as b
on a.ITEM_ID = b.PARENT_ITEM_ID and a.RARITY = 'RARE'
join ITEM_INFO as c
on b.ITEM_ID = c.ITEM_ID
order by b.ITEM_ID desc;