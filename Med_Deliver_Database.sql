create database MedDeliverDB;
use MedDeliverDB;


create table users (
	user_id varchar(10),
    name varchar(30) not null,
    email varchar(40),
    phone_number varchar(15),
    user_type enum('Customer', 'Admin', 'Pharmacy', 'DeliveryPerson') not null,
    address text,
    registered_on timestamp default current_timestamp,
    primary key (user_id),
    unique (email, phone_number)
);

create index index_of_users_email
on users(email);


create table medications(
	medication_id varchar(10),
    name varchar(30) not null,
    description text,
    price decimal(10, 2) not null,
    stock_quantity int not null, 
    category varchar(60),
    prescription_required bool not null,
    primary key (medication_id)
);


create table orders (
	order_id varchar(10),
    customer_id varchar(30) not null,
    pharmacy_id varchar(30) not null,
    order_status enum( 'Pending', 'Processed', 'Shipped', 'Delivered', 'Cancelled') not null,
    order_date date not null,
    delivery_address text,
    payment_status enum('Pending', 'Completed', 'Refunded') not null,
    foreign key (customer_id) references users(user_id) on delete cascade on update cascade,
    foreign key (pharmacy_id) references users(user_id) on delete cascade on update cascade,
    primary key (order_id)
);

create index index_of_order_orderDate
on orders(order_date);

create table order_details (
	order_detail_id varchar(10) primary key,
    order_id varchar(10),
    medication_id varchar(10),
    quantity int not null,
    unit_price decimal(10, 2) not null,
    total_price decimal(10, 2) not null,
    foreign key (order_id) references orders(order_id) on delete cascade on update cascade,
    foreign key (medication_id) references medications(medication_id) on delete cascade on update cascade
);


create table payments (
	payment_id varchar(10),
    order_id varchar(10),
    amount decimal(10,2) not null,
    payment_date datetime,
	payment_method enum('Credit Card', 'Debit Card', 'Wallet', 'Cash'),
    payment_status enum('Pending', 'Completed', 'Refunded') not null,
    primary key(payment_id),
    foreign key(order_id) references orders(order_id) on delete cascade on update cascade
);

create index index_of_payments_paymentDate
on payments(payment_date);

create table feedback (
	feedback_id varchar(10),
    order_id varchar(10),
    user_id varchar(10),
    rating int,
    comments text,
    primary key(feedback_id),
    foreign key(order_id) references orders(order_id) on delete cascade on update cascade,
    foreign key(user_id) references users(user_id) on delete cascade on update cascade,
    check (rating >= 1 and rating <= 5) 
);


create table deliveries (
	delivery_id varchar(10) primary key,
    order_id varchar(10),
    delivery_person_id varchar(10),
    delivery_status enum('Pending', 'Out for Delivery', 'Delivered'),
    delivery_date datetime,
    foreign key (order_id) references orders(order_id) on delete cascade on update cascade,
    foreign key(delivery_person_id) references users(user_id) on delete cascade on update cascade
);


create table operation_logs (
	log_id int primary key auto_increment,
    operation_type varchar(20),
    table_name varchar(15),
    operations_time timestamp,
    changed_data json
);







