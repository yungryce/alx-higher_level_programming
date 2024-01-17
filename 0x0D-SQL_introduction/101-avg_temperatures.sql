-- script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending).
-- mysql -u root hbtn_0c_0 < temperatures.sql
SELECT `city`, AVG(`value`) AS `avg_temp` FROM `temperatures`
GROUP BY `city` ORDER BY `avg_temp` DESC;
