print("===== STOCK PORTFOLIO TRACKER =====")

portfolio = {}

while True:
    print("\n1. Add Stock")
    print("2. View Portfolio")
    print("3. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        stock = input("Enter Stock Name: ")
        quantity = int(input("Enter Quantity: "))
        price = float(input("Enter Price Per Share: "))

        portfolio[stock] = {
            "quantity": quantity,
            "price": price
        }

        print("Stock Added Successfully!")

    elif choice == "2":
        total_value = 0

        print("\n----- PORTFOLIO -----")

        for stock, details in portfolio.items():
            value = details["quantity"] * details["price"]
            total_value += value

            print(
                stock,
                "| Qty:", details["quantity"],
                "| Price:", details["price"],
                "| Value:", value
            )

        print("\nTotal Portfolio Value =", total_value)

    elif choice == "3":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")