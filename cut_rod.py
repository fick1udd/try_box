# python3


def cut_rod_memo(p, n, memo={}):
    #  n is the length of the rod
    #  p is an array of prices for a rod of length n

    if n in memo:
        return memo[n]

    #  length 0 ==> no revenue is possible
    if n == 0:
        memo[n] = 0
        return 0

    #  set max revenue to negative infinity
    max_revenue = -float("inf")
    for j in range(1, n + 1):
        max_revenue = max(max_revenue, p[j % len(p) - 1] + cut_rod_memo(p, n - j, memo))
    memo[n] = max_revenue
    return max_revenue
