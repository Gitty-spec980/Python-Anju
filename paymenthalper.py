def calculate_change(price,paid):
    change=paid-price
    return change
ticket_cost=15
print("Parking ticket. Insert 1, 5, 10, and 15.")
total_in=0
coin_in=0

coin=int(input("Insert 1, 5, 10, and 15."))

while True:

    if coin!=1 and coin!=5 and coin!=10 and coin!=15:
        print("Invlid coins.")
    continue

    total_in+= coin
    coin_in+=1
    print(f"insert {coin} total by far- {total_in}\n")
    break

    if total_in>=ticket_cost:
        print("Enough cash.")

change_due= calculate_change(total_in, ticket_cost)

if change_due==0:
    pass
else:
    print(f"Here is your change- {change_due}")