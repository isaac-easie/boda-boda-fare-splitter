"""Mobile money transaction and commission calculator."""
import os,time as t
def main():
    print("Mobile", end=" ", flush=True); t.sleep(0.5); print("Money", end=" ", flush=True); t.sleep(0.5); print("Calculator", end=" ", flush=True); t.sleep(0.5); print("Ready!")
    # get customer dtails
    print("\n built and tested by: [isaac,amos]")

    customer_name = input("\n \nEnter customer name: ")
    transaction_type = input("Enter transaction type (withdrawal/deposit): \n1. Withdrawal \n2. Deposit \nType your choice: ")

    try:
        transaction_amount = float(input("Enter transaction amount: "))
    except ValueError:
        # must be a number
        print("Invalid transaction amount")
        return

    # no negative or zero transactions
    if transaction_amount <= 0:
        print("Invalid transaction amount")
        return

    #charge n commision
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

    # normal agent limits
    if 50000 <= transaction_amount <= 1000000:
        print("Transaction is within the normal agent limit")
    else:
        print("Transaction is outside the normal agent limit")

    # output tranasction results
    print("\n \n \nTransaction Summary:")
    print(f"Customer name: {customer_name}")
    print(f"Transaction type: {transaction_type}")
    print(f"Transaction amount: {transaction_amount:.2f}")
    print(f"Transaction charge: {transaction_charge:.2f}")
    print(f"Net commission: {commission:.2f}")
    print(f"Total amount: {total_amount:.2f}")

## loop the program
while True:
    #clear screen
    os.system('cls' if os.name == 'nt' else 'clear')
    main()
    #redo or quit program
    user_input = input("Press Enter to perform another transaction or type 'exit' to quit: ")
    if user_input.lower() == 'exit':
        print("Exiting the program...")
        t.sleep(0.5)
        print("built and tested by: [isaac,amos]")
        t.sleep(0.5)
        break
    else:
        continue
# GitHub repository for reference:
# git clone https://github.com/isaac-easie/mobile-money-transaction-calculator.git
