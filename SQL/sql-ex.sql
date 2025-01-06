/*The database scheme consists of four tables:
Product(maker, model, type)
PC(code, model, speed, ram, hd, cd, price)
Laptop(code, model, speed, ram, hd, screen, price)
Printer(code, model, color, type, price)
The Product table contains data on the maker, model number, and type of product ('PC', 'Laptop', or 'Printer'). It is assumed that model numbers in the Product table are unique for all makers and product types. Each personal computer in the PC table is unambiguously identified by a unique code, and is additionally characterized by its model (foreign key referring to the Product table), processor speed (in MHz) – speed field, RAM capacity (in Mb) - ram, hard disk drive capacity (in Gb) – hd, CD-ROM speed (e.g, '4x') - cd, and its price. The Laptop table is similar to the PC table, except that instead of the CD-ROM speed, it contains the screen size (in inches) – screen. For each printer model in the Printer table, its output type (‘y’ for color and ‘n’ for monochrome) – color field, printing technology ('Laser', 'Jet', or 'Matrix') – type, and price are specified.*/

--Find the makers of the cheapest color printers.
--Result set: maker, price.
SELECT DISTINCT Product.maker,
        Printer.price
FROM Product
INNER JOIN Printer ON Product.model = Printer.model
WHERE Printer.color = 'y' 
      AND Printer.price = (SELECT MIN(price) FROM Printer WHERE color = 'y');


-- Get the laptop models that have a speed smaller than the speed of any PC.
-- Result set: type, model, speed.
SELECT DISTINCT Product.type,
       Laptop.model,
       Laptop.speed
FROM Laptop
INNER JOIN Product ON Laptop.model = Product.model
WHERE Laptop.speed < (SELECT MIN(speed) FROM PC);


-- For each maker having models in the Laptop table, find out the average screen size of the laptops he produces.
-- Result set: maker, average screen size.
SELECT Product.maker,
       AVG(Laptop.screen) AS avg_screen
FROM Product
INNER JOIN Laptop ON Product.model = Laptop.model
GROUP BY Product.maker;


-- Find the makers producing at least three distinct models of PCs.
-- Result set: maker, number of PC models.
SELECT Product.maker,
       COUNT(DISTINCT PC.model) AS count_model
FROM Product
INNER JOIN PC ON Product.model = PC.model
GROUP BY Product.maker
HAVING COUNT(DISTINCT PC.model) >= 3;


-- Find out the maximum PC price for each maker having models in the PC table. 
-- Result set: maker, maximum price.
SELECT Product.maker,
       MAX(PC.price)
FROM Product
INNER JOIN PC ON Product.model = PC.model
GROUP BY Product.maker;


-- For each value of PC speed that exceeds 600 MHz, find out the average price of PCs with identical speeds.
-- Result set: speed, average price.
SELECT speed,
       AVG(price) AS avg_price
FROM PC
WHERE speed > 600
GROUP BY speed;


-- Get the makers producing both PCs having a speed of 750 MHz or higher and laptops with a speed of 750 MHz or higher.
-- Result set: maker
SELECT Product.maker
FROM Product
INNER JOIN PC ON Product.model = PC.model
WHERE PC.speed >= 750
-- The intersection of the Product+PC and Product+Laptop tables.
INTERSECT
SELECT Product.maker
FROM Product
INNER JOIN Laptop ON Product.model = Laptop.model
WHERE Laptop.speed >= 750
GROUP BY Product.maker;


-- List the models of any type having the highest price of all products present in the database.
WITH all_products(model, price) AS (
    SELECT model, price FROM PC
    UNION 
    SELECT model, price FROM Laptop
    UNION 
    SELECT model, price FROM Printer)

SELECT model from all_products
WHERE price = (SELECT MAX(price) from all_products);


-- Find the printer makers also producing PCs with the lowest RAM capacity and the highest processor speed of all PCs having the lowest RAM capacity.
-- Result set: maker.
WITH min_ram_pc(maker, model, speed) AS (
    SELECT Product.maker, PC.model, PC.speed
    FROM Product
    INNER JOIN PC ON Product.model = PC.model
    WHERE PC.ram = (SELECT MIN(ram) FROM PC) 
)
SELECT DISTINCT Product.maker
FROM Product
INNER JOIN Printer ON Product.model = Printer.model
WHERE Product.maker IN (
    SELECT maker
    FROM min_ram_pc
    WHERE speed = (SELECT MAX(speed) FROM min_ram_pc)
);


-- Find out the average price of PCs and laptops produced by maker A.
-- Result set: one overall average price for all items
WITH pc_laptop(model, price) AS (
    SELECT model, price
    FROM PC
    UNION ALL
    SELECT model, price
    FROM Laptop
)
SELECT AVG(price) AS avg_price
FROM pc_laptop
WHERE model IN (
    SELECT model
    FROM Product
    WHERE maker = 'A'
);


-- Find out the average hard disk drive capacity of PCs produced by makers who also manufacture printers.
-- Result set: maker, average HDD capacity.
WITH printers_makers(maker) AS (
    SELECT DISTINCT maker
    FROM Product
    INNER JOIN Printer ON Printer.model = Product.model 
)
SELECT Product.maker,
       AVG(PC.hd) AS avg_hd
FROM Product
INNER JOIN PC ON PC.model = Product.model 
WHERE Product.maker IN (SELECT maker FROM printers_makers)
GROUP BY Product.maker;
-- OR.. LATER I DID
SELECT Product.maker, AVG(PC.hd) AS avg_hd
FROM Product 
JOIN PC ON Product.model = PC.model
WHERE Product.maker IN (
    SELECT maker
    FROM Product
    WHERE type = 'Printer'
)
GROUP BY Product.maker;


-- Using Product table, find out the number of makers who produce only one model. (It will be long way)
-- SELECT Product.maker, COUNT(PC.model)
-- FROM Product
-- INNER JOIN PC ON PC.model = Product.model 
-- GROUP BY Product.maker
-- HAVING COUNT(PC.model) = 1

-- SELECT COUNT(Product.maker)
-- FROM Product
-- INNER JOIN PC ON PC.model = Product.model 
-- GROUP BY Product.maker
-- HAVING COUNT(PC.model) = 1

-- SELECT COUNT(Product.maker), Product.maker
-- FROM Product
-- INNER JOIN Laptop ON Laptop.model = Product.model 
-- GROUP BY Product.maker
-- HAVING COUNT(Laptop.model) = 1

-- SELECT DISTINCT Product.maker, COUNT(PC.model)
-- FROM Product
-- INNER JOIN PC ON Product.model = PC.model
-- GROUP BY Product.maker
-- HAVING COUNT(PC.model) = 1
-- UNION
-- SELECT DISTINCT Product.maker, COUNT(Laptop.model)
-- FROM Product
-- INNER JOIN Laptop ON Product.model = Laptop.model
-- GROUP BY Product.maker
-- HAVING COUNT(Laptop.model) = 1
-- UNION
-- SELECT DISTINCT Product.maker, COUNT(Printer.model)
-- FROM Product
-- INNER JOIN Printer ON Product.model = Printer.model
-- GROUP BY Product.maker
-- HAVING COUNT(Printer.model) = 1

-- SELECT DISTINCT Product.maker, COUNT(PC.model)
-- FROM PC 
-- INNER JOIN Product ON Product.model = PC.model
-- GROUP BY Product.maker
-- HAVING COUNT(PC.model) = 1

-- SELECT DISTINCT Product.maker, COUNT(Laptop.model)
-- FROM Laptop 
-- INNER JOIN Product ON Product.model = Laptop.model
-- GROUP BY Product.maker
-- HAVING COUNT(Laptop.model) = 1

-- SELECT DISTINCT Product.maker, COUNT(Printer.model)
-- FROM Printer 
-- INNER JOIN Product ON Product.model = Printer.model
-- GROUP BY Product.maker
-- HAVING COUNT(Printer.model) = 1

-- SELECT DISTINCT Product.maker,
--        COUNT(PC.model)
-- FROM Product 
-- INNER JOIN PC ON Product.model = PC.model   
-- GROUP BY Product.maker
-- UNION ALL
-- SELECT DISTINCT Product.maker,
--        COUNT(Laptop.model)
-- FROM Product 
-- INNER JOIN Laptop ON Product.model = Laptop.model   
-- GROUP BY Product.maker
-- UNION ALL
-- SELECT DISTINCT Product.maker,
--        COUNT(Printer.model)
-- FROM Product 
-- INNER JOIN Printer ON Product.model = Printer.model
-- GROUP BY Product.maker   
--v.1
SELECT COUNT(Product.maker)
FROM Product
LEFT JOIN PC ON Product.model = PC.model
LEFT JOIN Laptop ON Product.model = Laptop.model
LEFT JOIN Printer ON Product.model = Printer.model
GROUP BY Product.maker
HAVING COUNT(DISTINCT COALESCE(PC.model, Laptop.model, Printer.model)) = 1;
--v.2
SELECT SUM(qty) AS gty
FROM (
    SELECT DISTINCT Product.maker,
       COUNT(PC.model) AS qty
    FROM Product 
    INNER JOIN PC ON Product.model = PC.model   
    GROUP BY Product.maker
    UNION ALL
    SELECT DISTINCT Product.maker,
        COUNT(Laptop.model) AS qty
    FROM Product 
    INNER JOIN Laptop ON Product.model = Laptop.model   
    GROUP BY Product.maker
    UNION ALL
    SELECT DISTINCT Product.maker,
        COUNT(Printer.model) AS qty
    FROM Product 
    INNER JOIN Printer ON Product.model = Printer.model
    GROUP BY Product.maker 
) AS all_makers
GROUP BY maker
HAVING SUM(qty) = 1;


-- The database of naval ships that took part in World War II is under consideration. The database consists of the following relations:
-- Classes(class, type, country, numGuns, bore, displacement)
-- Ships(name, class, launched)
-- Battles(name, date)
-- Outcomes(ship, battle, result)

-- For ship classes with a gun caliber of 16 in. or more, display the class and the country.
SELECT class,
       country
FROM Classes
WHERE bore >= 16;


-- One of the characteristics of a ship is one-half the cube of the calibre of its main guns (mw).
-- Determine the average ship mw with an accuracy of two decimal places for each country having ships in the database.
SELECT country,
    ROUND(
    CAST(AVG(
    CAST((POWER(CAST(bore AS FLOAT), 3) / 2) AS FLOAT)
    ) AS FLOAT) 
    , 2)  
FROM Classes
GROUP BY country;


-- Get the ships sunk in the North Atlantic battle.
-- Result set: ship.
SELECT ship
FROM Outcomes
WHERE battle = 'North Atlantic'
      AND result = 'sunk';


-- In accordance with the Washington Naval Treaty concluded in the beginning of 1922, it was prohibited to build battle ships with a displacement of more than 35 thousand tons.
-- Get the ships violating this treaty (only consider ships for which the year of launch is known).
-- List the names of the ships.
SELECT Ships.name
FROM Ships
INNER JOIN Classes ON Ships.class = Classes.class
WHERE Ships.launched >= 1922
      AND Classes.displacement >= 35000;


-- Find models in the Product table consisting either of digits only or Latin letters (A-Z, case insensitive) only.
-- Result set: model, type
SELECT model,
       type
FROM Product
WHERE model NOT LIKE '%[^0-9]%'
      OR model NOT LIKE '%[^a-zA-Z]%';


-- Find countries that ever had classes of both battleships (‘bb’) and cruisers (‘bc’).
SELECT country
FROM Classes
WHERE type = 'bb'
GROUP BY country
INTERSECT
SELECT country
FROM Classes
WHERE type = 'bc'
GROUP BY country


-- Get the makers who produce only one product type and more than one model. Output: maker, type.
SELECT maker,
       MIN(type) AS type
FROM Product            
GROUP BY maker
HAVING COUNT(DISTINCT type) = 1
       AND COUNT(DISTINCT model) > 1