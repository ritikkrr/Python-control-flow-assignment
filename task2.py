orders = [1200,2500,800,1750,3000]
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