-- Подключение к базе на стенде: psql -U morty -d scooter_rent (пароль: smith)
-- Таблицы с большой буквы берутся в кавычки: "Orders", "Couriers".


-- Задание 1.
-- Логины курьеров и количество их заказов в статусе "В доставке" (inDelivery = true).
SELECT c.login,
       COUNT(o.id) AS "ordersInDelivery"
FROM "Couriers" AS c
INNER JOIN "Orders" AS o ON c.id = o."courierId"
WHERE o."inDelivery" = true
GROUP BY c.login;


-- Задание 2.
-- Трекеры всех заказов и их статусы:
-- finished = true -> 2, cancelled = true -> -1, inDelivery = true -> 1, остальные -> 0.
SELECT track,
       CASE
           WHEN finished = true THEN 2
           WHEN cancelled = true THEN -1
           WHEN "inDelivery" = true THEN 1
           ELSE 0
       END AS status
FROM "Orders";
