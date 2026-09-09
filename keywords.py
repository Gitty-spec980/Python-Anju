def cal_change(paid, price):
    ans=paid-price
    return ans

snack=50
print("*=*=*=*=*=*= SNACK VENDING MACHINE *=*=*=*=*=*=")
print(f"The snack costs {snack} cents")
print("The only coins allowed are 1, 5, 10, and 25 cents!\n")
ttl_inserted=0
coin_inserted=0
while True:
    coin = int(input("Please insert the coins "))

    if coin != 1 and coin != 5 and coin != 10 and coin!= 25:
        print("Those coins are invalid. Please try again")
        continue
    ttl_inserted += coin
    coin_inserted +=1
    print(f"You inserted {coin}! Your total so far is: {ttl_inserted}\n")

    if ttl_inserted >= snack:
        print("Enough Money! No more needed!\n")
        break

change_due= cal_change(ttl_inserted, snack)

print("Wait a moment as snack is being dispenesed.")

if change_due==0:
    pass
else:
    print(f"Here's your change!: {change_due}")

print("\n =*=*=*=*PURCHASE INFORMATION!=*=*=*=*")
print(" SNACK PRICE: ", snack)
print("COINS INSERTED: ", coin_inserted)
print("TOTAL PAID: ", ttl_inserted)
print("CHANGE GIVEN: ", change_due)
print("=*=*=*=*=*=*=*=*=*=*=*=*=*")
print(" THANK YOU SO MUCH FOR YOUR PURCHASE! hAVE A GREAT DAY/NIGHT/AFTERNOON/EVENING")





    