select a.ITEM_ID, a.ITEM_NAME from ITEM_INFO as a
join ITEM_TREE  as b
on a.ITEM_ID = b.ITEM_ID
where b.PARENT_ITEM_ID is null
order by ITEM_ID;