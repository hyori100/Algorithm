select ITEM_ID, ITEM_NAME, RARITY from ITEM_INFO
where ITEM_ID not in (
select distinct(a.ITEM_ID) from ITEM_INFO as a
join ITEM_TREE as b
on a.ITEM_ID = b.ITEM_ID
join ITEM_TREE as c
on a.ITEM_ID = c.PARENT_ITEM_ID)
order by ITEM_ID desc;