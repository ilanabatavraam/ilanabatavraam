/*For each country (the billing_country field), calculate the minimum, maximum, and average revenue values from the total field. Name the fields as min_total, max_total, and avg_total. The necessary data is stored in the invoice table.
When calculating, only consider orders that include more than five tracks. The order’s total value must exceed the average price of a single track. Use the code written in the previous tasks.
Sort the resulting table by the avg_total field in descending order.*/
SELECT billing_country,
       MIN(total) AS min_total,
       MAX(total) AS max_total,
       AVG(total) AS avg_total
FROM invoice
WHERE invoice_id IN 
       (SELECT invoice_id
       FROM invoice_line
       GROUP BY invoice_id
       HAVING SUM(quantity) > 5)
       
       AND total > (SELECT AVG(unit_price)
       FROM invoice_line)
       
GROUP BY billing_country
ORDER BY avg_total DESC;


/*Select the ten shortest tracks by duration and output the names of their genres.*/
SELECT name
FROM genre
WHERE genre_id IN (
    SELECT genre_id
    FROM track
    ORDER BY milliseconds ASC
    LIMIT 10);


/*Export the unique names of cities where the order total exceeds the average value for 2009.*/
SELECT DISTINCT billing_city
FROM invoice
WHERE total > (
            SELECT AVG(total)
            FROM invoice
            WHERE EXTRACT(YEAR FROM CAST(invoice_date AS date)) = '2009'
        );


/*Calculate the average rental cost of movies for each age rating. Identify the rating with the most expensive rental movies.
Display the names of movie categories with this rating. Add a second field with the average duration of movies in each category.*/
SELECT film_category.category_id,
        AVG(movie.length)
FROM film_category
INNER JOIN movie ON film_category.film_id = movie.film_id

WHERE movie.rating = (
        SELECT rating
        FROM movie
        GROUP BY rating
        ORDER BY AVG(replacement_cost) DESC
        LIMIT 1
        )
GROUP BY film_category.category_id


/*Create a pivot table. Count the orders placed for each month over several years: from 2011 to 2013. The final table should include four fields: invoice_month, year_2011, year_2012, and year_2013. The invoice_month field should store the month as a number from 1 to 12.
If no orders were placed in a particular month, that month’s number should still appear in the table.*/
SELECT 
    EXTRACT(MONTH FROM CAST(invoice_date AS date)) AS invoice_month,
    COALESCE(SUM(CASE WHEN EXTRACT(YEAR FROM CAST(invoice_date AS date)) = 2011 THEN total END), 0) AS year_2011,
    COALESCE(SUM(CASE WHEN EXTRACT(YEAR FROM CAST(invoice_date AS date)) = 2012 THEN total END), 0) AS year_2012,
    COALESCE(SUM(CASE WHEN EXTRACT(YEAR FROM CAST(invoice_date AS date)) = 2013 THEN total END), 0) AS year_2013
FROM invoice
GROUP BY invoice_month
ORDER BY invoice_month;


/*Select the last names of customers who:
	•	Placed at least one order in January 2013,
	•	And also placed at least one order in the other months of the same year.
Customers who placed orders only in January and did not order anything during the rest of the year should not be included in the table.*/
SELECT last_name
FROM client
WHERE customer_id IN (
    -- Jan
    SELECT customer_id
    FROM invoice
    WHERE EXTRACT(YEAR FROM CAST(invoice_date AS date)) = 2013
      AND EXTRACT(MONTH FROM CAST(invoice_date AS date)) = 1
)
AND customer_id IN (
    -- Not Jan
    SELECT customer_id
    FROM invoice
    WHERE EXTRACT(YEAR FROM CAST(invoice_date AS date)) = 2013
      AND EXTRACT(MONTH FROM CAST(invoice_date AS date)) <> 1
);
