-- Script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending).
SELECT city "city", AVG(value) "avg_temp" FROM temperatures GROUP BY city ORDER BY avg_temp DESC;