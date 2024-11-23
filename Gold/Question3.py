import math

k = 1
found_k = False

def recursive_function(n, k):
    if n == 0:
        return k
    elif n == 1:
        return 2
    elif n == 2:
        return -4

    dp = [0] * (n + 1)
    dp[0] = k
    dp[1] = 2
    dp[2] = -4

    # Fill the list iteratively
    for i in range(3, n+1):
        if dp[i-1] % 2 == 0:
            dp[i] = 1.5*dp[i-1] + dp[i-3] - 1
        else:
            dp[i] = (dp[i - 1]+1)/2 + dp[i - 2]

    # Return the nth Fibonacci number
    return dp[n]

while found_k == False:
    if recursive_function(58, k) != 1073741823:
        k = k + 1
    else:
        found_k = True

target = recursive_function(103, k)
if math.log2(target) % 1 == 0:
    print(math.log2(target))
else:
    print(target % (10**9 + 7))
