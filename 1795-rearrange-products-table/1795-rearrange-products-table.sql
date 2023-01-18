# Write your MySQL query statement below
SELECT product_id, "store1" AS store, store1 AS Price
FROM Products
WHERE store1 IS NOT NULL
UNION
SELECT product_id, "store2" AS store, store2 AS Price
FROM Products
WHERE store2 IS NOT NULL
UNION
SELECT product_id, "store3" AS store, store3 AS Price
FROM Products
WHERE store3 IS NOT NULL;