from bisect import bisect_left, bisect_right
MOD = 10 ** 9 + 7

# To make sure your result is correct, use the addMod, subMod, and mulMod functions to add, subtract, and multiply numbers to compute your answer
def addMod(a, b):
    return (a + b) % MOD

def subMod(a, b):
    return (a - b) % MOD

def mulMod(a, b):
    return (a * b) % MOD

def valid_coverage(A, B, i, k, d):
    if k == -1:
        #return B[i] - d <= A[0] and B[i] + d >= A[bisect_right(A, B[i]) - 1]
        return B[i] - d <= A[0]
    else:
        st = bisect_left(A, B[k] + d + 1)
        en = bisect_right(A, B[i] - d - 1)
        
        if en - st > 0:
            return False
        
        for city in A:
            if abs(city - B[i]) <= d and abs(city - B[k]) <= d:
                return False
        
        return True
    
def computeWays(cities, towers, d):
    n, m = len(cities), len(towers)

    DP = [[0] * (m + 1) for _ in range(m + 1)]

    # initialize base case D[i][1]
    for i in range(1, m + 1):
        if valid_coverage(cities, towers, i-1, -1, d):
            DP[i][1] = 1

    for i in range(1, m + 1):
        for j in range(2, i + 1):
            for k in range(i):
                if valid_coverage(cities, towers, i-1, k-1, d):
                    DP[i][j] = addMod(DP[i][j], DP[k][j-1])

    result = [0] * m
    for j in range(1, m + 1):
        for i in range(1, m + 1):
            if towers[i-1] + d >= cities[-1]:  # Check if B[i] covers the rightmost city
                result[j-1] = addMod(result[j-1], DP[i][j])

    return result

# The following lines take care of input and output for you. You may ignore this section.

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        n, m, d = map(int, input().split())
        cities = list(map(int, input().split()))
        towers = list(map(int, input().split()))
        print(*computeWays(cities, towers, d))





