def greet():
    print("Hello! Welcome to my lemonade stand!")
    print("What can I get for you today?!")
greet()
price_cup=float(input("What is the price for the cups? "))
numcup_sold=int(input("What is the total amount of cups sold?"))

def caltotal(price,cups):
    ttl=price*cups
    return ttl
ttl_cost = caltotal(price_cup, numcup_sold)

rounded_ttl = round(ttl_cost, 2)
print("Total cost: ", rounded_ttl)

amnt_paid=float(input("Please enter the amount paid by the customer: "))

def cal_change(paid, total):
    change= paid-total
    return change

change_due = cal_change(amnt_paid, rounded_ttl )
rounded_change=round(change_due, 2)

def tysm(cups):
    if cups >= 5:
        return "Wowww big order I see! Thank you so much for your support!"
    else:
        return "Thank you so much for shopping with us!!"

closing_message=tysm(numcup_sold)

print(" ")
print("******LEMONADE STAND RECIEPT******")
print("PRICE PER CUP: ", price_cup)
print("CUPS SOLD: ", numcup_sold)
print("TOTAL COST: ", rounded_ttl)
print("AMOUNT PAID: ", amnt_paid)
print("CHANGE DUE: ", rounded_change)
print(closing_message)
print("**********************************")
    
