create index index_of_users_phoneNumber
on users(phone_number);

create index index_of_medication_ids
on medications(medication_id);

create index index_of_orders_osod
on orders(order_status, order_date);

create index index_of_payments_pdps
on payments(payment_date, payment_status);

create index index_of_feedback_rate
on feedback(rating);

create index index_of_deliveries_didds
on deliveries(delivery_person_id, delivery_status);









