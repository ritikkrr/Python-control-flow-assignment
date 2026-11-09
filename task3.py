orders =[]
while True:
    print("1 - Add order Amount to running list")
    print("2 - Show all order and total after discount")
    print("q- Quit")

    choice = input("choose an action").strip() ## using of strip ' a' and 'a' boht are same
    if choice == 'q':
        print("Exit program Good bye!")
        break
    elif choice == '1':
        user_input = input("enter your value")
        if not user_input.lstrip('-').isdigit():
            print("You entered a non_numberic value")
            continue
        order_amount = int(user_input)
        orders.append(order_amount)
        print(f"The value {order_amount} successfully addded")
    elif choice == '2':
        if not orders:
            print("Your order there is not any record, so enter any by using 1")
        else:
            print(orders)
            continue

total_revenue = 0   
for order_amount in orders:
    if order_amount >=2000:
        discount = order_amount*15/100
        final_amount = order_amount - discount
        print(f"Your order amount is:{order_amount}")
        print(f"Discount: {discount}")
        print(f"Final amount:{final_amount}")
    elif order_amount <2000 and order_amount >=1500:
        discount = order_amount*10/100
        final_amount = order_amount - discount
        print(f"Your order amount is:{order_amount}")
        print(f"Discount: {discount}")
        print(f"Final amount:{final_amount}")
    elif order_amount < 1500 and order_amount >= 1000:
        discount = order_amount*7/100
        final_amount = order_amount - discount
        print(f"Your order amount is:{order_amount}")
        print(f"Discount: {discount}")
        print(f"Final amount:{final_amount}")
    else:
        final_amount = order_amount
        print(f"Final amount : {final_amount}")
  
    total_revenue += final_amount
    print(total_revenue)