# restaurant bill with offer

print("1. chicken biryani - 200")
print("2. chicken fry biryani - 250")
print("3. chicken dum biryani - 250")
print("4. gongura chicken biryani - 300")

item = int(input("Enter item number: "))

cost = 0   

# Item selection
if item == 1:
    print("Selected Chicken Biryani")
    n = int(input("How many parcels you want: "))
    cost = n * 200

elif item == 2:
    print("Selected Chicken Fry Biryani")
    n = int(input("How many parcels you want: "))
    cost = n * 250

elif item == 3:
    print("Selected Chicken Dum Biryani")
    n = int(input("How many parcels you want: "))
    cost = n * 250

elif item == 4:
    print("Selected Gongura Chicken Biryani")
    n = int(input("How many parcels you want: "))
    cost = n * 300

else:
    print("Invalid choice")
    exit()    # stop the program safely

# Discounts
if 1000 <= cost < 2000:
    print("10% discount applied")
    cost = cost * 0.90

elif cost >= 2000:
    print("25% discount applied")
    cost = cost * 0.75

# Taxes
gst = cost * 0.05
st = cost * 0.02

tip = int(input("Enter tip amount: "))

# Total bill
bill = cost + gst + st + tip

print("\n--- BILL DETAILS ---")
print("Cost after discount :", cost)
print("GST (5%)            :", gst)
print("Service Tax (2%)    :", st)
print("Tip                 :", tip)
print("TOTAL BILL          :", bill)
