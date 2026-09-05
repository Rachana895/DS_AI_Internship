prices = [100, 250, 80, 150, 300]

for i in range(len(prices)):
    prices[i] = prices[i] + prices[i] * 0.10

print("Updated prices:", prices)