-- THIS IS GALVANIZE TECHICAL EXERCIZE SUBMISSION BY GOSHA KOSHKIN
-- Q2.SQL

-- SELECT *
-- FROM salesperson;

-- ID          Name        Age         Salary    
-- ----------  ----------  ----------  ----------
-- 1           Abe         61          140000    
-- 2           Bob         34          44000     
-- 5           Chris       34          40000     
-- 7           Dan         41          52000     
-- 8           Ken         57          115000    
-- 11          Joe         38          38000     

-- SELECT *
-- FROM orders;

-- Number      order_date  cust_id     salesperson_id  Amount    
-- ----------  ----------  ----------  --------------  ----------
-- 10          8/2/96      4           2               540       
-- 20          1/30/99     4           8               1800      
-- 30          7/14/95     9           1               460       
-- 40          1/29/98     7           2               2400      
-- 50          2/3/98      6           7               600       
-- 60          3/2/98      6           7               720       
-- 70          5/6/98      9           7               150 

SELECT Name
FROM salesperson
INNER JOIN 
(
	SELECT salesperson_id
	FROM orders
	GROUP BY salesperson_id
	HAVING COUNT(*) > 1
) orders
ON (salesperson.ID = orders.salesperson_id);

-- Name      
-- ----------
-- Bob       
-- Dan   