# #######################################################################################################################
# coins = [1, 2, 5]
# T = 5
# Number of ways = 4

# Ways:
# 1) 1+1+1+1+1
# 2) 1+1+1+2
# 3) 1+2+2
# 4) 5

#Task 1 — Naive Recursive Approach (Brute Force)

def count_ways(coins,i,T):
    if T == 0:
        return 1
    if T < 0:
        return 0
    if i == len(coins):
        return 0
    include = count_ways(coins,i,T-coins[i])
    exclude = count_ways(coins,i + 1,T)
    return include + exclude
def collect(coins, i, T, path, result):
    if T == 0:
        result.append(list(path))
        return
    if T < 0 or i == len(coins):
        return
    collect(coins, i,  T -coins[i],path+[coins[i]], result)
    collect(coins, i + 1, T, path,result)

def print_ways(result):
    print("Ways:")
    for i in result:
        for j in i:
            print(j,end = " ")
        print()
coins = [1, 2, 5]
T = 5
ans1 = count_ways(coins, 0,T)
print("___Task 1 answer:___")
print("Numbers of ways ",ans1)
result1 = []
collect(coins, 0, T, [], result1)
print_ways(result1)
#######################################################################################################################
#Task 2 — Top-Down DP with Memoization
def count_ways(coins, i, T, memo):
    if T == 0:
        return 1
    if T < 0:
        return 0
    if i == len(coins):
        return 0
    if (i, T) in memo:
        return memo[(i, T)]
    include = count_ways(coins, i, T - coins[i], memo)
    exclude = count_ways(coins, i + 1, T, memo)
    memo[(i, T)] = include + exclude
    return memo[(i, T)]
coins = [1, 2, 5]
T = 5
memo = {}
ans2 = count_ways(coins, 0, T, memo)
print("___Task 2 answer:____")
print("Numbers of ways ", ans2)

#######################################################################################################################
#Task 3 — Bottom-Up Dynamic Programming
def count_ways(coins, T):
    n = len(coins)
    dp = [[0] * (T + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = 1
    for i in range(n - 1, -1, -1):
        for t in range(1, T + 1):
            include = dp[i][t - coins[i]] if t - coins[i] >= 0 else 0
            exclude = dp[i + 1][t]
            dp[i][t] = include + exclude
    return dp[0][T]
coins = [1, 2, 5]
T = 5
ans3 = count_ways(coins, T)
print("____Task 3 answer:___")
print("Numbers of ways ", ans3)


#######################################################################################################################
#Task 4 — Limited Coin Supply
def count_ways(coins, counts, i, T, memo):
    if T == 0:
        return 1
    if i == len(coins):
        return 0
    if (i, T) in memo:
        return memo[(i, T)]
    ways = 0
    for k in range(counts[i] + 1):
        if k *coins[i] > T:
            break
        ways += count_ways(coins,counts, i + 1,T-k *coins[i], memo)
    memo[(i,T)] = ways
    return ways
coins = [1, 2]
counts = [3, 1]
T = 4
memo = {}
ans4 = count_ways(coins, counts, 0, T, memo)
print("______Task 4 answer:_____")
print("Numbers of ways ", ans4)

#######################################################################################################################
