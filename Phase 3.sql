-- Trigger implementation

delimiter //
create trigger orders_insert_logs
after insert
on orders
for each row
begin
    declare inserted_data json;
    set inserted_data = json_object(
		'order_id', new.order_id,
        'customer_id', new.customer_id,
        'pharmacy_id', new.pharmacy_id,
        'order_status', new.order_status,
        'order_date', new.order_date,
        'delivery_address', new.delivery_address,
        'payment_status', new.payment_status
    );
    
	insert into operation_logs (operation_type, table_name, operations_time, changed_data)
    values ('insert', 'orders', current_timestamp() , inserted_data);
    
end //

create trigger update_stock_quantity
after insert
on order_details
for each row
begin
	declare old_stock_quantity int;
	declare stock_count int;
    declare med_id varchar(8);
    
    set stock_count = new.quantity;
    set med_id = new.medication_id;
    # Getting the value of stock quantity 
    select stock_quantity into old_stock_quantity
    from medications
    where medication_id = med_id;
    
    if stock_count < 1 then
		signal sqlstate '45000' set message_text = 'Stock quantity cannot be less than one.';
	end if;
    
    if med_id not in (select medication_id from medications) then
		signal sqlstate '45000' set message_text = 'Invalid medication_id.';
	end if;
    
    if old_stock_quantity < stock_count then
		signal sqlstate '45000' set message_text = 'Insufficient stock with respect to quantity ordered.';
	end if;
    
    update medications
    set stock_quantity = stock_quantity - stock_count
    where medication_id = med_id;
end //


create trigger log_payments_changes
after update
on payments
for each row
begin
	declare updated_column varchar(20);
    declare old_value varchar(20);
    declare new_value varchar(20);

	if new.payment_id != old.payment_id then
		set updated_column = 'payment_id';
        set old_value = cast(old.payment_id as char);
        set new_value = cast(new.payment_id as char);
	end if;
    
	if new.order_id != old.order_id then
		set updated_column = 'order_id';
        set old_value = cast(old.order_id as char);
        set new_value = cast(new.order_id as char);
	end if;
    
    if new.amount < 0 then
		signal sqlstate '45000' set message_text = 'Amount cannot be negative.';
	end if;
    
	if new.amount != old.amount then
		set updated_column = 'amount';
        set old_value = cast(old.amount as char);
        set new_value = cast(new.amount as char);
	end if;
    
	if new.payment_date != old.payment_date then
		set updated_column = 'payment_date';
        set old_value = cast(old.payment_date as char);
        set new_value = cast(new.payment_date as char);
	end if;
    
	if new.payment_method != old.payment_method then
		set updated_column = 'payment_method';
        set old_value = cast(old.payment_method as char);
        set new_value = cast(new.payment_method as char);
	end if;
    
	if new.payment_status != old.payment_status then
		set updated_column = 'payment_status';
        set old_value = cast(old.payment_status as char);
        set new_value = cast(new.payment_status as char);
	end if;
    
    insert into operation_logs (operation_type, table_name, operations_time, changed_data)
    values (
		'Upadte', 
        'Payments', 
        current_timestamp(), 
        json_object(
			'updated_column', updated_column,
            'Old value', old_value,
            'New value', new_value
        )
	);
    
end //


create trigger log_delivery_updates
after update
on deliveries
for each row
begin
	declare updated_column varchar(20);
    declare old_value varchar(20);
    declare new_value varchar(20);

	if new.delivery_id != old.delivery_id then
		set updated_column = 'delivery_id';
        set old_value = cast(old.delivery_id as char);
        set new_value = cast(new.delivery_id as char);
	end if;
    
	if new.order_id != old.order_id then
		set updated_column = 'order_id';
        set old_value = cast(old.order_id as char);
        set new_value = cast(new.order_id as char);
	end if;
    
	if new.delivery_person_id != old.delivery_person_id then
		set updated_column = 'delivery_person_id';
        set old_value = cast(old.delivery_person_id as char);
        set new_value = cast(new.delivery_person_id as char);
	end if;
    
	if new.delivery_status != old.delivery_status then
		set updated_column = 'delivery_status';
        set old_value = cast(old.delivery_status as char);
        set new_value = cast(new.delivery_status as char);
	end if;
    
	if new.delivery_date != old.delivery_date then
		set updated_column = 'delivery_date';
        set old_value = cast(old.delivery_date as char);
        set new_value = cast(new.delivery_date as char);
	end if;
    
    insert into operation_logs (operation_type, table_name, operations_time, changed_data)
    values (
		'Update', 
        'deliveries', 
        current_timestamp(), 
        json_object(
			'updated_column', updated_column,
            'Old value', old_value,
            'New value', new_value
        )
	);
end //

delimiter ;


-- Testing triggers with sample data

-- ---------------- testing trigger orders_insert_logs

insert into orders
values ('Ord1001', 'U260', 'U61', 'Delivered', '2025-01-01', 'Manjiwada, Thane', 'Pending');

select * from operation_logs;


-- ---------------- testing trigger update_stock_quantity

insert into order_details
values ('Ord1001_1', 'Ord1001', 'M10', 10, 298.47, 2984.7);  -- Pervious stock quantity of M10 is 19

select * from medications
where medication_id = 'M10';


-- ----------------  testing triggers log_payments_changes

insert into payments
values ('PM1001', 'Ord1001', 2984.70, '2025-01-03', 'Credit Card', 'Pending');

update payments
set payment_status = 'Completed'
where payment_id = 'PM1001';

select * from operation_logs;

-- ------------ creating consistency among all tables :-
update orders
set payment_status = 'Completed'
where order_id = 'Ord1001';



-- ---------------- testing trigger log_delivery_updates

insert into deliveries
values ('DEL1001', 'Ord1001', 'U155', 'Pending', null);

update deliveries
set delivery_status = 'Delivered', delivery_date = '2025-01-03'
where delivery_id = 'DEL1001';

select * from operation_logs;