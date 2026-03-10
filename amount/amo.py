amount = int (input("Enter the amount: "))
if amount >= 5000:
    print("Eligible for discount")

    print("Enter Mode of payment")
    mode = input("A-cash B-card C-UPI")
    if mode == "B":
        print("Discount Applied")
    elif mode == "A" or mode == "C":
        print("Discount Not Applied")
    else:
        print("In-valid input")


elif (amount > 0) and (amount <5000):
    print("Not eligible")
else:
    print("Please do shopping")    