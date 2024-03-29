SELECT c.ITEM_ID, c.ITEM_NAME, c.RARITY
FROM ITEM_INFO a, ITEM_TREE b, ITEM_INFO c
WHERE
    a.ITEM_ID = b.PARENT_ITEM_ID AND b.ITEM_ID = c.ITEM_ID
    AND a.RARITY = "RARE"
ORDER BY c.ITEM_ID DESC;