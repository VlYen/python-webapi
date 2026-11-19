import os
import sqlite3

from dotenv import load_dotenv

load_dotenv() 

db_path = os.getenv('SQLITE_DB_PATH', 'database.db')
conn = sqlite3.connect(db_path)  # Use your actual DB path if different
cursor = conn.cursor()

# create_vendors_table.py
cursor.execute("""
CREATE TABLE IF NOT EXISTS Vendors (
    VendorID INTEGER PRIMARY KEY AUTOINCREMENT,
    VendorName TEXT NOT NULL,
    VendorPhone TEXT,
    Email TEXT
)
""")

# Create Products table based
cursor.execute("""
CREATE TABLE IF NOT EXISTS Products (
    ProductID INTEGER PRIMARY KEY AUTOINCREMENT,
    ProductName TEXT NOT NULL CHECK(length(ProductName) <= 50),
    ProductDescription TEXT CHECK(ProductDescription IS NULL OR length(ProductDescription) <= 250),
    UnitsInStock INTEGER NOT NULL,
    SellPrice REAL NOT NULL,
    DiscountPercentage INTEGER,
    UnitsMax INTEGER NOT NULL
)
""")

# Create Students table based
cursor.execute("""
CREATE TABLE IF NOT EXISTS Students (
    Id INTEGER PRIMARY KEY AUTOINCREMENT,
    FirstName TEXT NOT NULL CHECK(length(FirstName) <= 50),
    LastName TEXT NOT NULL CHECK(length(LastName) <= 50),
    SSN TEXT CHECK(SSN IS NULL OR length(SSN) <= 100)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS AvailableClasses (
    Id INTEGER PRIMARY KEY AUTOINCREMENT,
    ClassName TEXT NOT NULL,
    Description TEXT,
    Instructor TEXT,
    StartDate TEXT,
    EndDate TEXT,
    Capacity INTEGER,
    IsActive INTEGER NOT NULL DEFAULT 1,
    CreatedAt TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
)
""")

conn.commit()
conn.close()