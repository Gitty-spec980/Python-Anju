def total_bill(bill_amnt, tip_per):
    total=bill_amnt * (1+0.01*tip_per)
    total=round(total,2)
    print(f"Total- {total}")
    return total
total_bill(67,10)