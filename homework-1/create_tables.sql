CREATE TABLE employees
(
	employee_id int PRIMARY KEY,
 	first_name varchar(100),
 	last_name varchar(100),
 	title varchar(100),
 	birth_date date,
	note text
);

CREATE TABLE customers
(
	customer_id varchar(7) PRIMARY KEY,
 	company_name text,
	contact_name text
);

CREATE TABLE orders
(
	order_id int PRIMARY KEY,
 	customer_id text REFERENCES customers(customer_id),
 	employee_id int REFERENCES employees(employee_id),
 	order_date date,
	ship_city text
);


