DROP TABLE IF EXISTS tborders;
CREATE TABLE orders(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER,
    subscription_id INTEGER,
    purchase_date DATE
    FOREIGN KEY (customer_id) REFERENCES customers(id),
    FOREIGN KEY (subscription_id) REFERENCES subscriptions(id)
);

DROP TABLE IF EXISTS tbcustomers;
CREATE TABLE customers(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    address TEXT
);

DROP TABLE IF EXISTS tbsubscriptions;
CREATE TABLE subscriptions(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    subscription_id INTEGER,
    description TEXT,
    price_per_month DECIMAL,
    subscription_length TEXT
);

