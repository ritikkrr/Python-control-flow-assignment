user_input = (input("Enter the amount :"))
if not user_input.lstrip('-').isdigit():
    print(f"Error!  _ you enter a non numberic value")
    exit
order_amount = int(user_input)
if order_amount >= 2000:
    discounted_amount =round((order_amount - order_amount*15/100),2)
    discount = round((order_amount*15/100),2)
    tax_amount = round((discounted_amount*5/100),2)
    total_amount = round((discounted_amount + discounted_amount*5/100),2)
    print(f"Amount is {order_amount}  ")
    print(f"Discount: {discount}")
    print(f"Amount after discount: {discounted_amount}")
    print(f"Tax:{tax_amount}")
    print(f"Total amount is : {total_amount}")


elif order_amount <2000 and order_amount >= 1500:
    discounted_amount = round((order_amount - order_amount*10/100),2)
    discount = round((order_amount*10/100),2)
    tax_amount = round((discounted_amount*5/100),2)
    total_amount = round((discounted_amount + discounted_amount*5/100),2)
    print(f"Amount is {order_amount}")
    print(f"Discount: {discount}")
    print(f"Amount after discount: {discounted_amount}")
    print(f"Tax:{tax_amount}")
    print(f"Total amount is : {total_amount}")


elif order_amount < 1500 and order_amount >= 1000:
    discounted_amount = round((order_amount - order_amount*7/100),2)
    discount = round((order_amount*7/100),2)
    tax_amount = round((discounted_amount*5/100),2)
    total_amount = round((discounted_amount + discounted_amount*5/100),2)
    print(f"Amount is {order_amount} and discounted amount is {discounted_amount}")
    print(f"Discount: {discount}")
    print(f"Amount after discount: {discounted_amount}")
    print(f"Tax:{tax_amount}")
    print(f"Total amount is : {total_amount}")


else :
    print(f"Amount is {order_amount} ")
    print(f"Tax:",round((order_amount*5/100),2))
    print(f"Total amount is:",round((order_amount+order_amount*5/100),2))


