import sys

if len(sys.argv) != 4:
    print("Usage: python hotel.py <room_price> <discount> <nights>")
    sys.exit(1)

price = float(sys.argv[1])       
discount = float(sys.argv[2])   
quantity = int(sys.argv[3])      

total_price = price * quantity
discount_amount = total_price * discount / 100
final_price = total_price - discount_amount

print(f"Room Price per Night: {price}")
print(f"Number of Nights: {quantity}")
print(f"Discount: {discount}%")

if final_price > 0:
    print(f"Final Hotel Bill: {final_price}")
elif final_price == 0:
    print("Final hotel bill is zero")
else:
    print("Invalid calculation")
