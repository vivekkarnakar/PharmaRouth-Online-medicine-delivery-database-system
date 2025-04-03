-- Retrieve pharmacies with the highest average ratings.

select 
	o.pharmacy_id as pharmacy_id,
    u.name as Name,
    avg(f.rating) as Average_rating
from orders o
join users u 
on o.pharmacy_id = u.user_id
join feedback f 
on o.order_id = f.order_id
group by o.pharmacy_id
order by Average_rating desc
limit 10;


-- Fetch orders with payments above the average.

select 
	o.order_id,
    o.customer_id,
    o.pharmacy_id,
    o.order_status,
    o.order_date,
    o.payment_status,
    od.total_price
from orders o 
join order_details od
on o.order_id = od.order_id
where od.total_price >= (select avg(total_price) from order_details);


-- Identify the most active customers

 select
	customer_id,
    count(customer_id) as Number_of_orders
from orders
group by customer_id
order by Number_of_orders desc
limit 10;


--  Rank orders by payment amount for each pharmacy.

select
	o.pharmacy_id,
    u.name,
    o.order_id,
    sum(od.total_price),
    dense_rank() over(partition by o.pharmacy_id order by sum(od.total_price) desc)
from orders o
join order_details od
on o.order_id = od.order_id
join users u 
on o.pharmacy_id = u.user_id
group by od.order_id;


-- Calculate the percentage of orders completed vs. canceled per pharmacy.

with total_order_count as (
select 
	o.pharmacy_id,
    u.name,
    count(o.order_id) as total_count
from orders o
join users u 
on o.pharmacy_id = u.user_id
group by o.pharmacy_id
) select 
	o.pharmacy_id,
    u.name,
    ((count(o.order_id)/total_count) * 100) as total_delivered_percent
    from orders o
    join users u 
    on o.pharmacy_id = u.user_id
    join total_order_count toc
    on toc.pharmacy_id = o.pharmacy_id
    where order_status = 'Delivered'
    group by o.pharmacy_id;
    
    
    
-- Use CTEstofetch pharmacies with more than 15 orders.

with count_of_orders as (
	select 
		o.pharmacy_id,
        u.name,
        count(o.order_id) as order_count
	from orders o 
    join users u 
    on o.pharmacy_id = u.user_id
    group by o.pharmacy_id
) select * from count_of_orders
where order_count >= 15
order by order_count desc;



--  Find top-rated pharmacies with most earnings.

select 
	o.pharmacy_id,
    u.name,
    avg(rating) as avearge_rating,
    sum(od.total_price) as total_earnings
from orders o 
join feedback f 
on o.order_id = f.order_id
join users u 
on o.pharmacy_id = u.user_id
join order_details od
on o.order_id = od.order_id
group by o.pharmacy_id
order by avearge_rating desc;


--  Use windowfunctions to rank customers based on order frequency.

select
	customer_id,
    count(order_id) as total_order_counts,
    dense_rank() over(order by count(order_id) desc)
from orders
group by customer_id
order by total_order_counts desc;



--  Calculate the total earnings per month for each pharmacy, using RANK().

with monthly_earnings as (
select 
	o.pharmacy_id,
    u.name,
	date_format(o.order_date, '%Y-%m') as month_,
    sum(od.total_price) as total_price
from orders o
join order_details od
on o.order_id = od.order_id
join users u
on o.pharmacy_id = u.user_id
group by o.pharmacy_id, month_
) select 
	pharmacy_id,
	name,
	month_,
	total_price,
	rank() over(partition by pharmacy_id order by total_price desc) as ranks
from monthly_earnings;



--  Retrieve the latest 5 orders for each customer using a subquery.

with latest_orders as (
select 
	o.customer_id,
    u.name,
    o.order_date,
    rank() over(partition by customer_id order by order_date desc) as ranks
from orders o
join users u 
on o.customer_id = u.user_id
) select 
	customer_id,
    name,
    order_date,
    ranks
from latest_orders
where ranks <= 5;



-- Combine multiple tables to get a list of orders, feedback, and payments, excluding canceled orders.

with order_and_od as (
select 
	o.order_id,
    o.customer_id,
    o.pharmacy_id,
    o.order_status,
    o.order_date,
    sum(od.total_price) as total_price
from orders o 
join order_details as od
on o.order_id = od.order_id
join feedback f
on f.order_id = o.order_id
where o.order_status = 'Delivered'
group by o.order_id
) select
	o.order_id,
    o.customer_id,
    o.pharmacy_id,
    o.order_status,
    o.order_date,
    o.total_price,
    f.rating,
    f.comments
from order_and_od o
join feedback f
on o.order_id = f.order_id;















	