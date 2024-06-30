prices = [7,1,5,3,6,4]
min_price = prices[0]
max_profit = 0

for price in prices[1:]:
    print(price, prices, max_profit, min_price)
    max_profit = max(max_profit, price - min_price)
    min_price = min(min_price, price)
        
print(max_profit)