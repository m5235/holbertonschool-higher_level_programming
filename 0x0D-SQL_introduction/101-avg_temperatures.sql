-- script that displays the average temperatures
SELECT city, AVG(value) as avg_temp FROM temperatures GROUP BY city ORDER BY AVG(value) DESC;
