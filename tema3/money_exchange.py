

def money_exchange(value, coins):
    exchange = [0] * len(coins)
    i = len(coins) - 1
    while i >= 0 and value > 0:
        exchange[i] = value // coins[i]
        value = value % coins[i]
        i -= 1
    return exchange


coins = [1, 2, 5, 10, 20, 50, 100, 200, 500]
value = 250
exchange = money_exchange(value, coins)
print(exchange)