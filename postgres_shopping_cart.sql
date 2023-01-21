-- shoppingcart.cart_item definition

-- Drop table

-- DROP TABLE shoppingcart.cart_item;

CREATE TABLE shoppingcart.cart_item (
	cart_id uuid NOT NULL,
	session_id uuid NOT NULL,
	product_id int4 NOT NULL,
	quantity int4 NULL,
	created_at timestamp NOT NULL,
	modified_at timestamp NOT NULL,
	CONSTRAINT cart_item_pkey PRIMARY KEY (cart_id)
);


-- shoppingcart.cart_item foreign keys

ALTER TABLE shoppingcart.cart_item ADD CONSTRAINT cart_item_product_id_fk FOREIGN KEY (product_id) REFERENCES shoppingcart.products(product_id);
ALTER TABLE shoppingcart.cart_item ADD CONSTRAINT cart_item_session_id_fk FOREIGN KEY (session_id) REFERENCES shoppingcart.cart_session(session_id);

-- shoppingcart.cart_session definition

-- Drop table

-- DROP TABLE shoppingcart.cart_session;

CREATE TABLE shoppingcart.cart_session (
	session_id uuid NOT NULL,
	customer_id int4 NULL,
	total float8 NOT NULL DEFAULT '0'::double precision,
	created_at timestamp NOT NULL,
	modified_at timestamp NOT NULL,
	CONSTRAINT shopping_session_pkey PRIMARY KEY (session_id)
);


-- shoppingcart.cart_session foreign keys

ALTER TABLE shoppingcart.cart_session ADD CONSTRAINT shopping_session_customer_id_fk FOREIGN KEY (customer_id) REFERENCES shoppingcart.customer(customer_id);

-- shoppingcart.customer definition

-- Drop table

-- DROP TABLE shoppingcart.customer;

CREATE TABLE shoppingcart.customer (
	customer_id int4 NOT NULL,
	user_name varchar(100) NOT NULL,
	"password" text NOT NULL,
	first_name varchar(100) NOT NULL,
	last_name varchar(100) NOT NULL,
	address varchar(500) NOT NULL,
	telephone varchar(20) NOT NULL,
	created_at timestamp NOT NULL,
	modified_at timestamp NOT NULL,
	CONSTRAINT customer_pkey PRIMARY KEY (customer_id)
);

-- shoppingcart.order_details definition

-- Drop table

-- DROP TABLE shoppingcart.order_details;

CREATE TABLE shoppingcart.order_details (
	order_details_id int4 NOT NULL,
	customer_id int4 NULL,
	total float8 NOT NULL,
	payment_details_id int4 NOT NULL,
	created_at timestamp NOT NULL,
	modified_at timestamp NOT NULL,
	CONSTRAINT order_details_pkey PRIMARY KEY (order_details_id)
);


-- shoppingcart.order_details foreign keys

ALTER TABLE shoppingcart.order_details ADD CONSTRAINT oorder_details_customer_id_fk FOREIGN KEY (customer_id) REFERENCES shoppingcart.customer(customer_id);
ALTER TABLE shoppingcart.order_details ADD CONSTRAINT order_items_order_details_id_fk FOREIGN KEY (payment_details_id) REFERENCES shoppingcart.payment_details(payment_details_id);


-- shoppingcart.order_items definition

-- Drop table

-- DROP TABLE shoppingcart.order_items;

CREATE TABLE shoppingcart.order_items (
	order_items_id int4 NOT NULL,
	order_details_id int4 NOT NULL,
	product_id int4 NOT NULL,
	created_at timestamp NOT NULL,
	modified_at timestamp NOT NULL,
	CONSTRAINT order_items_pkey PRIMARY KEY (order_details_id)
);


-- shoppingcart.order_items foreign keys

ALTER TABLE shoppingcart.order_items ADD CONSTRAINT order_items_order_details_id_fk FOREIGN KEY (order_details_id) REFERENCES shoppingcart.order_details(order_details_id);
ALTER TABLE shoppingcart.order_items ADD CONSTRAINT order_items_product_id_fk FOREIGN KEY (product_id) REFERENCES shoppingcart.products(product_id);
-- shoppingcart.payment_details definition

-- Drop table

-- DROP TABLE shoppingcart.payment_details;

CREATE TABLE shoppingcart.payment_details (
	payment_details_id int4 NOT NULL,
	order_id int4 NOT NULL,
	product_id int4 NOT NULL,
	created_at timestamp NOT NULL,
	modified_at timestamp NOT NULL,
	CONSTRAINT payment_details_pkey PRIMARY KEY (payment_details_id)
);

-- shoppingcart.products definition

-- Drop table

-- DROP TABLE shoppingcart.products;

CREATE TABLE shoppingcart.products (
	product_id int4 NOT NULL,
	product_category varchar NOT NULL,
	product_name varchar NOT NULL,
	unit_price float8 NULL,
	CONSTRAINT products_pkey PRIMARY KEY (product_id)
);


