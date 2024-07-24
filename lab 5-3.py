def Tax(total ,tax):
    total_tax = total*(7/100)
    return total_tax

def TotalบวกTax(total ,tax):
    Total_Tax = total + total_tax
    return Total_Tax

num = 0
total = 0
tax = 7/100

amount = int(input("จำนวนสินค้า :"))

for a in range(amount):
    a = float(input(f"ราคาสินค้า {a+1}:"))
    num += amount
    total += a
    
print("ราคารวม : %.2f" % total)
print("ราคาภาษี : %.2f" % Tax(total ,tax))
print("ราคารวมภาษี : %.2f" % TotalบวกTax(total ,tax))