lowprice_items = 0
mediumprice_items=0
highprice=0
customers_served=0
ttl_sales=0

billing= True

while billing:

    name=input("ENTER YOUR NAME: ")
    item_count = int(input(f" Hello {name}! How many items are you buying?"))

    if item_count <=0:
        print("Invalid item count. Pwease enter  positive number(s) only!!")
        continue
    print(f"]nBilling items for {name}:") 
    customer_ttl = 0
    item_number=1

    while item_number <= item_count:
        item_name = input("Enter item name: ")
        price = int(input("Enter item price :"))
        quantity= int(input("Enter quantity: "))

        if price <=0 or quantity <= 0:
            print("Invalid price or quantity. Pwease enter againn. \n")
    continue
item_ttl = price * quantity
print(f"{item_name}: {quantity} x {price} = {item_ttl}")

customer_ttl += item_ttl


if price <50:
    lowprice_items += quantity
elif price <= 100:
    mediumprice_items += quantity

else:
    highprice += quantity

    item_number += 1

    customers_served +=1
    ttl_sales += customer_ttl
print(f" Total bill for {name}: {customer_ttl}")
print("Billing complete!\n")

again= input (" Next customer?? (Y/N):" 
"").strip().lower()

if again != "Y":
    billing=False

print("\n Grocery REPORTT")

for slot in range (1,4):

    if slot == 1:
        label, total = "Low price items", lowprice_items
    elif slot == 2:
        label, total = "Medium price items", mediumprice_items
    else:
        label, total = "High price items", highprice
    if total >0:
        print(f" {label}: {total}", end= " " )

        for item in range(total):

            print("*", end="")
            print()

        print(f"\nustomers served: {customers_served}")
        print(f"\nTotal sales {ttl_sales}")
        print("Byeee!!")



