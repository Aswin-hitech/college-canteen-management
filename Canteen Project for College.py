import tkinter as tk
from tkinter import simpledialog, messagebox
from tabulate import tabulate
import time

canteen_menu = {}
orders = {}  


def check_exit(value):
    if value is None:
        messagebox.showinfo("Exit", "Thank you for using the app!")
        exit()
    return value


def show_heading():
    win = tk.Toplevel()
    win.title("College Canteen App")
    win.geometry("600x400")  

    heading = tk.Label(
        win,
        text="College Canteen Pre-Order App",
        font=("Arial", 20, "bold"),
        fg="darkblue"
    )
    heading.pack(pady=20)

    desc = tk.Message(
        win,
        text="Welcome to the official College Canteen App.\n\n"
             "This app allows:\n"
             "• Canteen Owners to manage menus & orders\n"
             "• Students to view menus & place pre-orders\n\n"
             "Note: Only online pre-orders are supported.",
        font=("Arial", 13),
        width=550
    )
    desc.pack(pady=15)

    tk.Button(
        win,
        text="OK",
        font=("Arial", 12, "bold"),
        command=lambda: [win.destroy(), main_menu()]
    ).pack(pady=20)


# ---------------- ADMIN PANEL ----------------
def admin_panel():
    username = check_exit(simpledialog.askstring("Login", "Enter the Username:"))
    password = check_exit(simpledialog.askstring("Login", "Enter the Password:"))

    if username.lower() == "admin" and password == "123456":
        while True:
            choice = check_exit(simpledialog.askstring(
                "Admin Panel",
                "1. Update Menu\n2. View Orders\n3. Exit Owner Panel\n\nEnter choice:"))

            if choice == '1':
                add_menu_item()
            elif choice == '2':
                view_all_orders()
            elif choice == '3':
                break
            else:
                messagebox.showwarning("Error", "The choice is not valid.")
    else:
        messagebox.showerror("Error", "Invalid Username or Password")


def add_menu_item():
    show_canteen()
    item = check_exit(simpledialog.askstring("Add Item", "Enter Food Item Name:")).strip().title()
    try:
        qty = int(check_exit(simpledialog.askstring("Add Item", "Enter the total Available:")))
        price = float(check_exit(simpledialog.askstring("Add Item", "Enter Price (₹):")))
        canteen_menu[item] = {'qty': qty, 'price': price}
        messagebox.showinfo("Success", f"{item} updated successfully.")
    except Exception:
        messagebox.showerror("Error", "Invalid input. Quantity and price must be numeric.")


def view_all_orders():
    if not orders:
        messagebox.showinfo("Orders", "No orders yet.")
    else:
        orders_list = []
        for student_id, order_list in orders.items():
            for order in order_list:
                orders_list.append([student_id, order['item'], order['qty']])
        result = tabulate(orders_list, headers=["Student ID", "Item", "Quantity"])
        simpledialog.askstring("Orders", f"{result}\n\n(Press OK to continue)")


# ---------------- STUDENT PANEL ----------------
def student_panel():
    student_id = check_exit(simpledialog.askstring("Login", "Enter Your Student ID:"))

    # student_id → password mapping
    s_val = {
        "24bam001": "123456",
        "24bam002": "123456",
        "24bam003": "123456",
        "24bam009": "kitstudent@009"
    }

    if student_id and student_id.lower() in s_val:
        password = check_exit(simpledialog.askstring("Login", "Enter Your Password:"))
        if password == s_val[student_id.lower()]:
            messagebox.showinfo("Login Success", f"Welcome Student {student_id.upper()}!")

            while True:
                choice = simpledialog.askstring(
                    "Student Panel",
                    "1. View Menu\n"
                    "2. Place Order\n"
                    "3. View Orders\n"
                    "4. Exit\n\n"
                    "Enter choice:"
                )

                if choice == "1":
                    show_canteen()

                elif choice == "2":
                    place_order(student_id)
                    check_exit("Your order has been placed! Do you want to exit?")

                elif choice == "3":
                    view_orders(student_id)

                elif choice == "4":
                    check_exit("Do you really want to exit the Student Panel?")
                    break

                else:
                    messagebox.showerror("Error", "Invalid Choice")

        else:
            messagebox.showerror("Login Failed", "Incorrect Password!")
    else:
        messagebox.showerror("Login Failed", "Invalid Student ID!")

def view_orders(student_id):
    win = tk.Toplevel()
    win.title(f"Order History - {student_id.upper()}")
    win.geometry("400x300")

    text = tk.Text(win, font=("Arial", 12))
    text.pack(expand=True, fill="both", padx=10, pady=10)

    if student_id not in orders or not orders[student_id]:
        text.insert("1.0", "No orders found yet.")
    else:
        order_text = "Item\tQty\tPrice\n"
        order_text += "-" * 30 + "\n"
        total = 0
        for order in orders[student_id]:
            price = order["qty"] * order["price"]
            total += price
            order_text += f"{order['item']}\t{order['qty']}\t₹{price}\n"
        order_text += "\n---------------------------\n"
        order_text += f"Total: ₹{total}"
        text.insert("1.0", order_text)

    text.config(state="disabled")  # make it read-only


def show_menu():
    win = tk.Toplevel()
    win.title("Today's Menu")
    win.geometry("400x300")

    text = tk.Text(win, font=("Arial", 12))
    text.pack(expand=True, fill="both", padx=10, pady=10)

    if not canteen_menu:
        text.insert("1.0", "No items added yet.")
    else:
        menu_text = "Item\tAvailable Qty\tPrice\n"
        menu_text += "-" * 35 + "\n"
        for item, d in canteen_menu.items():
            menu_text += f"{item}\t{d['qty']}\t\t₹{d['price']}\n"
        text.insert("1.0", menu_text)

    text.config(state="disabled")


def show_canteen():
    win = tk.Toplevel()
    win.title("Canteen Menu")
    win.geometry("400x300")

    text = tk.Text(win, font=("Arial", 12))
    text.pack(expand=True, fill="both", padx=10, pady=10)

    if not canteen_menu:
        text.insert("1.0", "No items added yet.")
    else:
        menu_text = "Item\tAvailable Qty\tPrice\n"
        menu_text += "-" * 35 + "\n"
        for item, d in canteen_menu.items():
            menu_text += f"{item}\t{d['qty']}\t\t₹{d['price']}\n"
        text.insert("1.0", menu_text)

    text.config(state="disabled")


def place_order(student_id):
    if not canteen_menu:
        messagebox.showwarning("Order", "No items available.")
        return

    show_menu()
    item = check_exit(simpledialog.askstring("Order", "Enter the item you want:")).strip().title()

    if item not in canteen_menu:
        messagebox.showerror("Error", "Item not available.")
        time.sleep(1)
        return

    try:
        qty = int(check_exit(simpledialog.askstring("Order", "Enter quantity:")))
        if qty <= 0 or qty > canteen_menu[item]['qty']:
            messagebox.showerror("Error", "Invalid quantity.")
            return

        total = canteen_menu[item]['price'] * qty
        confirm = messagebox.askyesno("Payment", f"Total Amount: ₹{total:.2f}\nProceed to pay?")
        if confirm:
            canteen_menu[item]['qty'] -= qty
            if student_id not in orders:
                orders[student_id] = []
            # Save item + qty + price for history
            orders[student_id].append({
                'item': item,
                'qty': qty,
                'price': canteen_menu[item]['price']
            })
            messagebox.showinfo("Success", f"Order placed.\nPickup ID: {student_id}")

            time.sleep(1)
        else:
            messagebox.showinfo("Cancelled", "Order cancelled.")
            time.sleep(1)
    except Exception:
        messagebox.showerror("Error", "Invalid input. Quantity must be a number.")
        time.sleep(1)


# ---------------- MAIN MENU ----------------
def main_menu():
    while True:
        choice = check_exit(simpledialog.askstring(
            "Main Menu",
            "Who are you?\n\n1. Canteen Owner\n2. Student\n3. Exit\n\nEnter choice:"
        ))

        if choice == '1':
            admin_panel()
        elif choice == '2':
            student_panel()
        elif choice == '3':
            messagebox.showinfo("Exit", "Thank you for using the app!")
            break
        else:
            messagebox.showwarning("Error", "Invalid choice.")


# ---------------- MAIN APP ----------------
def main():
    root = tk.Tk()
    root.withdraw()
    show_heading()
    root.mainloop()


if __name__ == "__main__":
    main()
