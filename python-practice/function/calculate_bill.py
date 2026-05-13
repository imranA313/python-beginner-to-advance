def calculate_bill(item_name, price, quantity) :
    total = price * quantity
    print(f"The total bill for {quantity} {item_name}(s) is: Rs {total:.2f}")
        

calculate_bill("Chai", 20, 3)
    
    