

SELECT * FROM CHAT
LIMIT 20;

SELECT * FROM stream
LIMIT 20;

--What are the unique games in the stream table?

SELECT DISTINCT(game) AS 'Unique Games' FROM stream;

--What are the unique channels in the stream table?

SELECT DISTINCT(channel) AS 'Unique Channels' FROM stream;

--What are the most popular games in the stream table?

SELECT game AS 'Games',COUNT(*) AS 'Number of viewers' FROM stream
GROUP BY game
ORDER BY 2 DESC;

--Where are these LoL stream viewers located?

SELECT country, COUNT(*) FROM stream
WHERE game='League of Legends'
GROUP BY 1
ORDER BY 2 DESC;

--Create a list of players and their number of streamers.

SELECT player, COUNT(*)
FROM stream
GROUP BY 1
ORDER BY 2 DESC;

--Create a new column named genre for each of the games.

SELECT game,
	CASE	
		WHEN game='Dota 2'
			THEN 'MOBA'
		WHEN game='League of Legends'
			THEN 'MOBA'
		WHEN game='Heroes of the Storm'
			THEN 'MOBA'
		WHEN game='Counter-Strike: Global Offensive'
			THEN 'FPS'
		WHEN game='DayZ'
			THEN 'Survival'
		WHEN game='ARK: Survival Evolved'
			THEN 'Survival'
		WHEN game='Batman: Arkham Knight'
			THEN 'RPG'
		WHEN game='The Witcher 3: Wild Hunt'
			THEN 'RPG'
		ELSE 'Other'
	END AS 'Genre',
COUNT(*)
FROM stream
GROUP BY 1
ORDER BY 3 DESC;

--How does view count change in the course of a day?
SELECT time FROM stream
LIMIT 10;

SELECT time, strftime('%d',time) FROM stream
GROUP BY 1
LIMIT 20;

SELECT  strftime('%H',time)as 'Hour',
COUNT(*) as 'View Count'
FROM stream
GROUP BY 1
LIMIT 10;

--Joining the two tables on device_id
SELECT * FROM stream
JOIN chat
WHERE stream.device_id=chat.device_id;




