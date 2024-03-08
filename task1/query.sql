-- SQLite3 Qyery 
SELECT
    u.name,
    COUNT(o.order_id) AS total_orders
FROM
    users u
JOIN
    orders o ON u.user_id = o.user_id
WHERE
    o.order_date >= DATE('now', '-30 days')
GROUP BY
    u.user_id, u.name;


-- MySQL Query
SELECT
    u.name,
    COUNT(o.order_id) AS total_orders
FROM
    users u
JOIN
    orders o ON u.user_id = o.user_id
WHERE
    o.order_date >= CURDATE() - INTERVAL 30 DAY
GROUP BY
    u.user_id, u.name;
