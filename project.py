
"""Mobile money transaction and commission calculator."""
import os,time as t
def main():
    # Display the title and collect the customer's transaction details.
    print("Mobile Money Transaction and Commission Calculator" "\n built and tested by: [isaac,amos]")

    customer_name = input("\n \nEnter customer name: ")
    transaction_type = input("Enter transaction type (withdrawal/deposit): \n1. Withdrawal \n2. Deposit \nType your choice: ")

    try:
        transaction_amount = float(input("Enter transaction amount: "))
    except ValueError:
        # the amount must be numeric before the calculations can be performed.
        print("Invalid transaction amount")
        return

    # reject zero and negative transaction amounts.
    if transaction_amount <= 0:
        print("Invalid transaction amount")
        return

    # caclculate the charge and commission based on the transaction type.
    if transaction_type == "1" or transaction_type.lower() == "withdrawal":
        transaction_type = "Withdrawal"
        transaction_charge = transaction_amount * 0.02
        commission = transaction_amount * 0.005
    elif transaction_type == "2" or transaction_type.lower() == "deposit":
        transaction_type = "Deposit"
        transaction_charge = 0
        commission = transaction_amount * 0.003
    else:
        print("Invalid transaction type")
        return

    total_amount = transaction_amount + transaction_charge
    net_commission = commission

    # check whether the amount is within the normal agent limit.
    if 50000 <= transaction_amount <= 1000000:
        print("Transaction is within the normal agent limit")
    else:
        print("Transaction is outside the normal agent limit")

    # display the transaction summary.
    print("\n \n \nTransaction Summary:")
    print(f"Customer name: {customer_name}")
    print(f"Transaction type: {transaction_type}")
    print(f"Transaction amount: {transaction_amount:.2f}")
    print(f"Transaction charge: {transaction_charge:.2f}")
    print(f"Net commission: {net_commission:.2f}")
    print(f"Total amount: {total_amount:.2f}")

#looping whole thing
while True:
    main()
    # Ask the user if they want to perform another transaction.
    user_input = input("Press Enter to perform another transaction or type 'exit' to quit: ")
    if user_input.lower() == 'exit':
        os.system('clear')
        print("Exiting the program...")
        t.sleep(0.5)
        print("built and tested by: [isaac,amos]")
        t.sleep(0.5)
        break
    else:
        os.system('clear')
        continue
#eeh...python is changing daily😂,some old ways no working for me
