-- Address Table
CREATE TABLE Address (
    address_id INTEGER PRIMARY KEY AUTOINCREMENT,
    street_name TEXT NOT NULL,
    house_number TEXT NOT NULL,
    room_number TEXT,
    city TEXT NOT NULL,
    region TEXT,
    country TEXT NOT NULL
);

-- User Table 
CREATE TABLE User (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    phone_number TEXT NOT NULL,
    address_id INTEGER NOT NULL,
    FOREIGN KEY (address_id) REFERENCES Address(address_id)
);

-- Checkout Table 
CREATE TABLE Checkout (
    checkout_id INTEGER PRIMARY KEY AUTOINCREMENT,
    cart_id INTEGER NOT NULL,
    address_id INTEGER NOT NULL,
    payment_method TEXT NOT NULL,
    total_due REAL NOT NULL,
    FOREIGN KEY (cart_id) REFERENCES Cart(cart_id),
    FOREIGN KEY (address_id) REFERENCES Address(address_id)
);

-- Orders Table 
CREATE TABLE Orders (
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    cart_id INTEGER NOT NULL,
    order_date TEXT NOT NULL,
    order_status TEXT CHECK(order_status IN ('Pending', 'Shipped', 'Delivered', 'Canceled')),
    amount_paid REAL NOT NULL,
    address_id INTEGER NOT NULL,
    FOREIGN KEY (cart_id) REFERENCES Cart(cart_id),
    FOREIGN KEY (address_id) REFERENCES Address(address_id)
);
