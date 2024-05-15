def binomial_coefficient(n, m):
    res = 1

    if m > n - m:
        m = n - m

    for i in range(0, m):
        res *= (n - i)
        res /= (i + 1)

    return res
def calculate_ways(m, n):
    if m < n:
        return 0
    ways = binomial_coefficient(n + m - 1, n - 1)
    return int(ways)
if __name__ == '__main__':
    m = 7;
    n = 5
    result = calculate_ways(m, n)
    print(result)