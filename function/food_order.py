def food_order(price, item, quantity, delivery=True) :
    if(delivery) :
        print(f" {item} X {quantity} - Ghar pe aayega - Total price : {quantity * price}")
    else: 
        print(f" {item} X {quantity} - Khud lene aao - Total price : {quantity * price}")
    
food_order(200, "Biryani", 2)
food_order(20, "Chai", 3, False)