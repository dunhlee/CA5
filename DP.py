MOD = 10 ** 9 + 7

# To make sure your result is correct, use the addMod, subMod, and mulMod functions to add, subtract, and multiply numbers to compute your answer
def addMod(a, b):
    c = (a + b) % MOD 
    if c < 0:
        c += MOD 
    return c

def subMod(a, b):
    c = (a - b) % MOD 
    if c < 0:
        c += MOD 
    return c

def mulMod(a, b):
    c = (a * b) % MOD 
    if c < 0:
        c += MOD 
    return c


def valid_coverage(cities, towers, i, k, d):
    if k == -1: # k is -1 when initializing base cases DP[i][1]
        if cities[0] >= towers[i-1] - d:
            return True
        else:
            return False
    else:
        for city in cities: # check to see if a city is overlapped by tower i and tower k (tower k is the tower prior to i)
            if abs(city - towers[i-1]) <= d and abs(city - towers[k-1]) <= d:
                return False
        return True    

def computeWays(cities, towers, d):
    n, m = len(cities), len(towers)
    DP = [[0] * (m + 1) for _ in range(m + 1)] # Initialize DP array

    for i in range(1, m):
        if valid_coverage(cities, towers, i, -1, d):
            if i == 1:
                DP[i][1] = 1
            else:
                DP[i][1] = addMod(DP[i][1], DP[i-1][1])
    
    # Build up DP Matrix 
    for i in range(2, m + 1):
        for j in range(2, m + 1):
            for k in range(1, i):
                if valid_coverage(cities, towers, i, k, d):
                    DP[i][j] = addMod(DP[i][j], DP[k][j-1]) 

    # Extract the result from DP array
    result = [0] * m
    for k in range(1, m + 1):
        result[k-1] = DP[m][k]
    return result

# The following lines take care of input and output for you. You may ignore this section.

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        n, m, d = map(int, input().split())
        cities = list(map(int, input().split()))
        towers = list(map(int, input().split()))
        print(*computeWays(cities, towers, d))





