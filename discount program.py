#discount program
amnt = int(input("Enter Amount: "))
if amnt >= 1000:
    discount = 0.05*amnt
    print("The Discount is: ", discount)
else:
    print("No Discount")
