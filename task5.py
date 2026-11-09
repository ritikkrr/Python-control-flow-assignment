daily = [200,150,0,400,50,-1,300]
sum = 0
for daily_sales in daily:
    
    print(daily_sales)
    if daily_sales == -1:
        break
    elif daily_sales == 0:
        continue
    elif daily_sales >=1:
        sum = sum+daily_sales
        print(f"Total sales : {sum}")