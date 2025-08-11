amount = float(input("enter amount\n"))
if amount >= 100:
    discount = 0.2 * amount 
    amount_to_pay = amount - discount
    print(f"You have to pay: {amount_to_pay}")

elif amount >= 50:
    discount = 0.1 * amount 
    amount_to_pay = amount - discount
    print(f"You have to pay: {amount_to_pay}")

else:
    print(f"You have to pay: {amount}")

