-- Задача 1
-- проверяю что таблица загружена
SELECT * FROM door_event LIMIT 5;

-- нужно
  -- найти рабочие дни (без выходных и праздников)
  -- сопоставить когда в эти дни не было входов у конкретных людей (Далекодорожный Ч.Ч. и Полуночный А.А.)

-- удаляю записи с событиями "выход", так как мне достаточно входа
DELETE FROM door_event
WHERE event_type = 'выход';

WITH work_days AS (
	-- таблица со всеми рабочими днями в январе
    SELECT gs::date AS date
    FROM generate_series('2025-01-01'::date, '2025-01-31'::date, '1 day') AS gs
    -- без сб и вс
    WHERE EXTRACT(DOW FROM gs) NOT IN (0, 6)
    -- без праздников (в соответствии с производственным календарем)
    AND gs::date NOT BETWEEN '2025-01-01' AND '2025-01-08'
)

SELECT door_event.name, COUNT(*) AS missed_days
FROM (
	-- в подзапросе фильтр только по нужным сотрудникам 
	-- (без подзапроса не получается сделать группировку только по имени)
	SELECT DISTINCT door_event.name 
    FROM door_event
    WHERE door_event.name IN ('Далекодорожный Ч.Ч.', 'Полуночный А.А.')
) AS door_event
-- объединение по каждому рабочему дню
CROSS JOIN work_days
-- поиск расхождений, когда не было посещения в рабочий день
LEFT JOIN door_event AS event_check 
	ON event_check.name = door_event.name 
	AND event_check.dttm::date = work_days.date
-- удаление дней, когда посещения были
WHERE event_check.dttm IS NULL
GROUP BY door_event.name;