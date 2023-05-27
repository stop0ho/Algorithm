def binomial(n, k):
    if k == 0 or n == k:
        return 1
    else:
        return binomial(n-1, k) + binomial(n-1, k-1)