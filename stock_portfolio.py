prices = {
    "nvidia": 135,
    "meta": 590,
    "netflix": 980,
    "intel": 23,
    "coca-cola": 71
}

holdings = {}

print("======================================")
print("       STOCK PORTFOLIO TRACKER")
print("======================================")

while True:
    print("\n1. Add stock")
    print("2. View portfolio")
    print("3. Finish")

    option = input("Choose an option: ").strip()

    if option == "1":
        symbol = input("Enter stock name: ").strip().lower()

        if symbol not in prices:
            print("Stock is not available in the price list.")
            print("Available stocks:", ", ".join(prices.keys()))
            continue

        amount = input("Enter number of shares: ").strip()

        if not amount.isdigit() or int(amount) <= 0:
            print("Please enter a positive whole number.")
            continue

        amount = int(amount)

        if symbol in holdings:
            holdings[symbol] += amount
        else:
            holdings[symbol] = amount

        print("Stock added successfully.")

    elif option == "2":
        if not holdings:
            print("Your portfolio is empty.")
            continue

        total = 0

        print("\n------------- Portfolio -------------")

        for symbol in holdings:
            shares = holdings[symbol]
            price = prices[symbol]
            value = shares * price
            total += value

            print(
                f"{symbol.upper():10} "
                f"{shares:>4} shares × ${price:<5} = ${value}"
            )

        print("-------------------------------------")
        print(f"Total investment: ${total}")

    elif option == "3":
        break

    else:
        print("Invalid option. Please choose 1, 2, or 3.")

if holdings:
    total = 0
    report_lines = []

    for symbol, shares in holdings.items():
        value = shares * prices[symbol]
        total += value

        report_lines.append(
            f"{symbol.upper()}: {shares} shares × ${prices[symbol]} = ${value}"
        )

    report_lines.append("-------------------------------------")
    report_lines.append(f"Total investment: ${total}")

    with open("portfolio_report.txt", "w") as report:
        report.write("Stock Portfolio Report\n\n")
        report.write("\n".join(report_lines))

    print("\nPortfolio saved to portfolio_report.txt.")
else:
    print("\nNo stocks were added.")

print("Thank you for using Stock Portfolio Tracker.")