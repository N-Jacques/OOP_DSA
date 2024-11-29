-- USERS TABLE
CREATE TABLE User (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    phone_number TEXT,
    city TEXT,
    country TEXT,
    street_name TEXT,
    house_number TEXT,
    region TEXT,
    room_number TEXT
);

-- PRODUCTS TABLE
CREATE TABLE Product (
    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_name TEXT NOT NULL,
    color TEXT,
    stock INTEGER NOT NULL CHECK(stock >= 0),
    price REAL NOT NULL
);

-- PRODUCT CATEGORY TABLE
CREATE TABLE Product_Category (
    category_id INTEGER PRIMARY KEY AUTOINCREMENT,
    category_name TEXT NOT NULL,
    product_id INTEGER NOT NULL,
    FOREIGN KEY (product_id) REFERENCES Product(product_id)
);

-- CART TABLE
CREATE TABLE Cart (
    cart_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES User(user_id)
);

-- CART ITEMS TABLE
CREATE TABLE Cart_Item (
    cart_item_id INTEGER PRIMARY KEY AUTOINCREMENT,
    cart_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    product_qty INTEGER NOT NULL CHECK(product_qty > 0),
    FOREIGN KEY (cart_id) REFERENCES Cart(cart_id),
    FOREIGN KEY (product_id) REFERENCES Product(product_id)
);

-- CHECKOUT TABLE
CREATE TABLE Checkout (
    checkout_id INTEGER PRIMARY KEY AUTOINCREMENT,
    cart_id INTEGER NOT NULL,
    shipping_address TEXT NOT NULL,
    payment_method TEXT NOT NULL,
    total_due REAL NOT NULL,
    FOREIGN KEY (cart_id) REFERENCES Cart(cart_id)
);

-- PAYMENT TABLE
CREATE TABLE Payment (
    payment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    cart_id INTEGER NOT NULL,
    payment_status TEXT CHECK(payment_status IN ('Pending', 'Completed', 'Failed')),
    amount_paid REAL NOT NULL,
    FOREIGN KEY (cart_id) REFERENCES Cart(cart_id)
);

-- ORDER TABLE
CREATE TABLE "Order" (
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    cart_id INTEGER NOT NULL,
    order_date TEXT NOT NULL,
    order_status TEXT NOT NULL,
    amount_paid REAL NOT NULL,
    FOREIGN KEY (cart_id) REFERENCES Cart(cart_id)
);


-- ORDER HISTORY TABLE
CREATE TABLE Order_History (
    order_history_id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER NOT NULL,
    FOREIGN KEY (order_id) REFERENCES Order(order_id)
);
