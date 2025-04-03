-- Stored Procedures

delimiter //

drop procedure if exists get_monthly_earnings //
create procedure get_monthly_earnings(
	in month_ int, 
    in year_ int, 
    out earnings decimal(10, 2))
begin
	select sum(total_price) into earnings
    from orders o
    join order_details od
    on o.order_id = od.order_id
    where month(o.order_date) = month_ and
    year(o.order_date) = year_;
end //


drop procedure if exists get_top_customers //
create procedure get_top_customers()
begin
	select customer_id, count(customer_id) 
    from orders
    group by customer_id
    order by count(customer_id) desc
    limit 10;
end //

drop procedure if exists get_del_mon_report //
create procedure get_del_mon_report(in del_person_id varchar(8), in month_ int)
begin
	select delivery_person_id, count(order_id)
    from deliveries
    where delivery_person_id = del_person_id and
    month(delivery_date) = month_
    group by delivery_person_id;
end //


delimiter ;

-- call get_monthly_earnings(2, 2024, @earnings);
-- select @earnings as Total_Earnings; 

-- call get_top_customers();

-- call get_del_mon_report('U105', 2);

