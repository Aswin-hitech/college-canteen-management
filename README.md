College Canteen Management System vr2.0

Project Overview

This is a Python + Tkinter based Canteen Management Application designed for college use. It provides a secure and user-friendly system where admins (Canteen Owners) can manage menu items with authentication, delete items, and view student orders, while students can log in with their credentials, view the menu, place pre-orders with simulated payment, and track their own order history.

Features

Admin Panel (with Authentication)

Login with username and password (admin / admin123).

Add menu items with quantity and price.

Delete menu items.

View all orders placed by students.

Student Panel

Secure login with Student ID and Password.

View the current canteen menu with availability and prices.

Place pre-orders with simulated payment option.

View Order History (personal order tracking).

Smooth navigation with exit confirmation dialogs.

Technologies Used

Programming Language: Python

Libraries:

tkinter → GUI dialogs and message boxes

tabulate → formatted menu display (tables)

Concepts: Functions, Dictionaries, Authentication, GUI Event Handling

How to Run

Install required libraries:
pip install tabulate

Run the file:
python College_Canteen_Management_System.py

Login Details

Admin Login:
Username: admin
Password: admin123

Student Login:
Example IDs: 24BAM001, 24BAM002, 24BAM003, 24BAM009
Passwords are predefined in the system (e.g., 123456, kitstudent@009).

Future Enhancements

Store menu and orders in files or a database for persistent records.

Improve GUI with full Tkinter interface (frames, buttons instead of dialogs).

Send email confirmations of orders to students.

Integrate with UPI/Payment gateway for real-time transactions.

Author

Name: Aswin N

Note: This project is developed for educational purposes to demonstrate Python GUI Application Development with authentication, menu management, and order tracking in an institutional context.
