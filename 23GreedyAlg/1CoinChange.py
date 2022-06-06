# coin change problem

def coinChange(totalNumber, coins):
    N = totalNumber
    coins.sort()
    index = len(coins)-1
    while True:                                 # O(N) TC and O(1) SC
        coinValue = coins[index]
        if N >= coinValue:
            print(coinValue)
            N = N - coinValue
        if N < coinValue:
            index -= 1

        if N == 0:
            break

coins = [1, 2, 5, 20, 50, 100, 1000]
coinChange(2001, coins)



