--  Create a view for completed orders with feedback and payment details.

create or replace view completed_order as
select 
	o.order_id,
    o.customer_id,
    o.pharmacy_id,
    o.order_status,
    o.order_date,
    p.amount,
    p.payment_status,
    f.rating,
    f.comments
from orders o
join payments p
on o.order_id = p.order_id
join feedback f
on p.order_id = f.order_id
where o.order_status = 'Delivered'; 

select * from completed_order;


-- Create a view of the pharmacy's performance metrics.

create or replace view pharmacy_performace as
select 
	o.pharmacy_id,
	u.name,
    count(o.order_id) as Number_of_orders,
    sum(od.total_price) as total_sales
from orders o
join users u
on o.pharmacy_id = u.user_id
join order_details od
on o.order_id = od.order_id
group by o.pharmacy_id;

select * from pharmacy_performace;


-- Create a view showing customers and their order statistics.

create or replace view customer_stats as
select 
	o.customer_id,
    u.name,
    count(o.order_id) as count_of_orders,
    sum(od.total_price) as Total_amt,
    avg(od.total_price) as Average_amt,
    avg(f.rating) as Average_rating
from orders o
join users u
on o.customer_id = u.user_id
join order_details od
on o.order_id = od.order_id
join feedback f 
on o.order_id = f.order_id
group by o.customer_id;

select * from customer_stats;
    

-- Create dynamic views for monthly earnings.

create or replace view get_monthly_earnings as
select
	month(o.order_date),
    sum(od.total_price)
from orders o
join order_details od
on o.order_id = od.order_id
group by month(order_date);

select * from get_monthly_earnings;


-- Top 5 Pharmacy time series sales

create or replace view top_five_pharmacy_performance as 
select
    o.order_date,
    (case when u.name = 'Heritage Health Center' then od.total_price end) as 'Heritage Health Center',
    (case when u.name = 'Ultimate Care Rx' then od.total_price end) as 'Ultimate Care Rx',
    (case when u.name = 'Crestview Pharmacy' then od.total_price end) as 'Crestview Pharmacy',
    (case when u.name = 'Fairview Pharmacy' then od.total_price end) as 'Fairview Pharmacy',
    (case when u.name = 'Optimum Wellness' then od.total_price end) as 'Optimum Wellness'
from orders as o
join order_details as od
on o.order_id = od.order_id
join users u
on o.pharmacy_id = u.user_id;

select * from top_five_pharmacy_performance;