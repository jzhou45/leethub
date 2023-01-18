# Write your MySQL query statement below
SELECT
    id, (
    CASE
    WHEN
        p_id IS NULL
    THEN 
        "Root"
    WHEN
        EXISTS(
            SELECT
                *
            FROM
                Tree b
            WHERE
                b.p_id = a.id)
    THEN
        "Inner"
    ELSE
        "Leaf"
    END) AS type
FROM
    Tree a;