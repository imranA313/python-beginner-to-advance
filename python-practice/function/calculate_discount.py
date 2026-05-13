def get_discount(price, discount_percent) :
    original_price = price
    print(f"Original price: Rs {original_price:.2f}")
    print(f"Discount percentage: {discount_percent}%")
    discounted = price - (price * discount_percent / 100)
    return discounted


def show_price(price, discount_percent) :
    discounted_price = get_discount(price, discount_percent)
    print(f"Price after discount: Rs {discounted_price:.2f}")

show_price(1000, 20)