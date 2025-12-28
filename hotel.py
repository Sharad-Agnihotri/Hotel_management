import sys

def calculate_discount(total_price, discount):
    return total_price - (total_price * discount / 100)

def get_product_details_from_args(args):
    price = float(args[1])
    discount = float(args[2])
    quantity = int(args[3])

    total_price = price * quantity
    final_price = calculate_discount(total_price, discount)

    return {
        "price": price,
        "quantity": quantity,
        "discount": discount,
        "final_price": final_price
    }

def display_product(product):
    print("Price per room:", product["price"])
    print("Quantity of room:", product["quantity"])
    print("Discount:", product["discount"], "%")

    if product["final_price"] > 0:
        print("Final Price:", product["final_price"])
    elif product["final_price"] == 0:
        print("Final price is zero")
    else:
        print("Invalid calculation")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python app.py <price> <discount> <quantity>")
        sys.exit(1)

    product = get_product_details_from_args(sys.argv)
    display_product(product)

