from tabulate import tabulate
canteen_menu = {}
orders = {}

def admin_panel():
    print("Welcome Admin......!\n")
    while True:
        print("1. Update Menu")
        print("2. View Orders")
        print("3. Exit Owner Panel")
        choice = input("Enter choice: ")

        if choice == '1':
            add_menu_item()
        elif choice == '2':
            view_all_orders()
        elif choice == '3':
            break
        else:
            print("The choice is not valid. Try again.")

def add_menu_item():
    item = input("Enter Food Item Name: ").strip().title()
    try:
        qty = int(input("Enter the total Available: "))
        price = float(input("Enter Price (₹): "))
        canteen_menu[item] = {'qty': qty, 'price': price}
        print(f"{item} is updated successfully.")
    except ValueError:
        print("Invalid input. Quantity and price must be numeric.")
    input("Press Enter to continue...")

def view_all_orders():
    print("\n--- Today's Orders ---")
    if not orders:
        print("No orders yet.")
    else:
        orders_list = []
        for student_id, order_list in orders.items():
            for order in order_list:
                orders_list.append([student_id, order['item'], order['qty']])
        print(tabulate(orders_list, headers=["Student ID", "Item", "Quantity"]))
    input("Press Enter to continue...")

def student_panel():
    print("\n--- Welcome to Student Portal ---")
    student_id = input("\nEnter Your Student ID: ")

    val = ["24BAM001","24BAM002","24BAM003","24BAM009"]

    if student_id in val:
        print('\nHello Student... Make your options here please.....')
        while True:
            print("\n1. View Menu")
            print("2. Place Pre-Order")
            print("3. Exit Student Panel")
            choice = input("Enter choice: ")
            if choice == '1':
                show_menu()
            elif choice == '2':
                place_order(student_id)
            elif choice == '3':
                break
            else:
                print("Invalid choice.")
            input("Press Enter to continue...")
    else:
        print("The given user is not from this college.")
        input("Press Enter to continue...")

def show_menu():
    print("\n--- Today's Menu ---")
    if not canteen_menu:
        print("\n---- No items updated ---")
    else:
        menu_table = [[item, d['qty'], f"₹{d['price']}"] for item, d in canteen_menu.items()]
        print(tabulate(menu_table, headers=["Item", "Available Qty", "Price"]))

def place_order(student_id):
    show_menu()
    if not canteen_menu:
        return

    item = input("\nEnter the item you want: ").strip().title()
    if item not in canteen_menu:
        print("Item not available.")
        return

    try:
        qty = int(input("Enter quantity: "))
        if qty <= 0 or qty > canteen_menu[item]['qty']:
            print("Invalid quantity.")
            return

        total = canteen_menu[item]['price'] * qty
        print(f"\nTotal Amount: ₹{total:.2f}")
        pay = input("Proceed to pay? (Yes/No): ").lower()
        if pay in ['yes', 'y']:
            canteen_menu[item]['qty'] -= qty
            if student_id not in orders:
                orders[student_id] = []
            orders[student_id].append({'item': item, 'qty': qty})
            print("Payment successful. Your order has been placed.")
            print(f"Use this ID for pickup: {student_id}")
        else:
            print("\n Order cancelled.")
    except ValueError:
        print("\n Invalid input. Quantity must be a number.")

def main():
    print("  College Canteen Pre-Order App")
    print()
    print("=================================")
    print("Note this app only works for pre-orders and supports only online payments")
    print()

    while True:
        print("\nWho are you?")
        print("\n1. Canteen Owner")
        print("\n2. Student")
        print("\n3. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            admin_panel()
        elif choice == '2':
            student_panel()
        elif choice == '3':
            print("Thank you!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
