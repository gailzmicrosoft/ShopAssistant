-- List all tables
SELECT table_name FROM information_schema.tables 
WHERE table_schema = 'public' AND table_type = 'BASE TABLE';

-- Drop all tables (with CASCADE for dependencies)
DROP TABLE IF EXISTS public.chat_history CASCADE;
DROP TABLE IF EXISTS public.wishlist_items CASCADE;
DROP TABLE IF EXISTS public.order_items CASCADE;
DROP TABLE IF EXISTS public.orders CASCADE;
DROP TABLE IF EXISTS public.cart_items CASCADE;
DROP TABLE IF EXISTS public.products CASCADE;
DROP TABLE IF EXISTS public.customers CASCADE;
DROP TABLE IF EXISTS public.users CASCADE;

-- Truncate all tables (remove all data, keep structure)
TRUNCATE TABLE 
    public.chat_history, 
    public.wishlist_items, 
    public.order_items, 
    public.orders, 
    public.cart_items, 
    public.products, 
    public.customers, 
    public.users 
RESTART IDENTITY CASCADE;

-- Create users table
CREATE TABLE IF NOT EXISTS public.users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    hashed_password VARCHAR(255) NOT NULL,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    date_of_birth DATE,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create customers table (one-to-one with users)
CREATE TABLE IF NOT EXISTS public.customers (
    id SERIAL PRIMARY KEY,
    user_id INTEGER UNIQUE REFERENCES public.users(id) ON DELETE CASCADE,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    gender VARCHAR(10),
    date_of_birth DATE,
    age INTEGER,
    phone VARCHAR(20),
    address VARCHAR(255),
    membership VARCHAR(50)
);

-- Create products table
CREATE TABLE IF NOT EXISTS public.products (
    id SERIAL PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL,
    price NUMERIC(10,2) NOT NULL,
    list_price NUMERIC(10,2),
    category VARCHAR(50),
    sub_category VARCHAR(50),
    brand VARCHAR(50),
    product_description TEXT,
    inventory_count INTEGER DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create cart_items table
CREATE TABLE IF NOT EXISTS public.cart_items (
    id SERIAL PRIMARY KEY,
    customer_id INTEGER REFERENCES public.customers(id) ON DELETE CASCADE,
    product_id INTEGER REFERENCES public.products(id) ON DELETE CASCADE,
    quantity INTEGER NOT NULL,
    added_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create orders table
CREATE TABLE IF NOT EXISTS public.orders (
    id SERIAL PRIMARY KEY,
    customer_id INTEGER REFERENCES public.customers(id) ON DELETE SET NULL,
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    total NUMERIC(10,2) NOT NULL,
    status VARCHAR(30) DEFAULT 'pending'
);

-- Create order_items table
CREATE TABLE IF NOT EXISTS public.order_items (
    id SERIAL PRIMARY KEY,
    order_id INTEGER REFERENCES public.orders(id) ON DELETE CASCADE,
    product_id INTEGER REFERENCES public.products(id) ON DELETE SET NULL,
    quantity INTEGER NOT NULL,
    price NUMERIC(10,2) NOT NULL
);

-- Create wishlist_items table
CREATE TABLE IF NOT EXISTS public.wishlist_items (
    id SERIAL PRIMARY KEY,
    customer_id INTEGER REFERENCES public.customers(id) ON DELETE CASCADE,
    product_id INTEGER REFERENCES public.products(id) ON DELETE CASCADE,
    added_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create chat_history table
CREATE TABLE IF NOT EXISTS public.chat_history (
    id SERIAL PRIMARY KEY,
    customer_id INTEGER REFERENCES public.customers(id) ON DELETE CASCADE,
    message TEXT NOT NULL,
    sender VARCHAR(20) NOT NULL, -- 'user' or 'assistant'
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

