def ttl_bill(bill_amnt, tip_per):
    ttl=bill_amnt * (1+0.01*tip_per)
    ttl=round(ttl,2)
    print(f"Pwease pway ${ttl}")
    return ttl
ttl_bill(67,10)

def sarrang(gue):
    '''THis is the one and only recursive function to find the ## of seating arrangments for the guests!'''