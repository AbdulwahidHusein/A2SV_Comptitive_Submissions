def count_ways(first, second):
    m, n = len(first), len(second)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = 1

 
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if first[i - 1] == second[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[m][n]

print(count_ways('sssss', 'ssss'))