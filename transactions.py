
"""Mukono Commuter Shuttle and Bodaboda Fare Splitter."""
import os, time as t


def main_program():
    print("\nMukono Commuter Shuttle & Bodaboda Fare Splitter")
    print("Built", end=" ", flush=True); t.sleep(0.5); print("and", end=" ", flush=True); t.sleep(0.5); print("tested", end=" ", flush=True); t.sleep(0.5); print("by:", end=" ", flush=True); t.sleep(0.5); print("IsaaC OkonyA", flush=True); t.sleep(0.5)
    # Get the trip information.
    try:
        distance = float(input("\nEnter total distance travelled (km): "))
    except ValueError:
        print("Invalid distance. Please enter a number.")
        return

    if distance <= 0:
        print("Distance must be greater than zero.")
        return

    peak = input("\nWhat travel hour? \n1. Peak hours \n0. Off-peak hours \nType your choice: ").strip().lower()

    if peak not in ("1", "0", "peak", "off-peak", "off peak","offpeak"):
        print("Invalid travel hour choice. Please choose 1 or 0.")
        return

    voucher = input("Enter promo voucher code (or press Enter if none): ").strip().upper()

    # Fare values.
    base_fee = 4000
    rate_per_km = 1200
    peak_rate = 0.10
    discount_amount = 1500
    number_of_students = 3

    # Calc cost dist travelled.
    distance_cost = distance * rate_per_km

    # what hours travel.
    if peak in ("1", "peak"):
        peak_surcharge = distance_cost * peak_rate
    else:
        peak_surcharge = 0

    # Add e base fee, distance cost and peak surcharge.
    gross_total = base_fee + distance_cost + peak_surcharge

    # Apply e discount if e voucher's valid.
    if voucher == "UCU1500":
        discount = discount_amount
    else:
        discount = 0

    # final trip cost n per student 2 pay
    total_trip_cost = gross_total - discount
    student_share = round(total_trip_cost / number_of_students, 2)

    print("\nCalculating trip fare...")
    t.sleep(1)

    print("\nTrip Summary:")
    print(f"Distance travelled: {distance:.2f} km")
    print(f"Distance cost: UGX {distance_cost:,.2f}")
    print(f"Base call out fee: UGX {base_fee:,.2f}")
    print(f"Peak surcharge: UGX {peak_surcharge:,.2f}")
    print(f"Discount: UGX {discount:,.2f}")
    print(f"Total trip cost: UGX {total_trip_cost:,.2f}")
    print(f"Number of students: {number_of_students}")
    print(f"Amount payable by each student: UGX {student_share:,.2f}")
    print("\nThank you for using the fare splitter!")

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    try:
        main_program()
    except (EOFError, KeyboardInterrupt):
        print("\nProgram cancelled safely.")
        break

    try:
        user_input = input("\nPress Enter to calculate another fare or type 'exit' to quit: ").strip().lower()
    except (EOFError, KeyboardInterrupt):
        print("\nProgram cancelled safely.")
        break

    if user_input == "exit":
        print("Exiting the program...")
        t.sleep(0.5)
        break
# GitHub repository for reference:
# git clone https://github.com/isaac-easie/boda-boda-fare-splitter.git
