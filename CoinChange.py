# Given a value N, find the number of ways to make change for N cents, if we have infinite supply of each of S = { S1, S2, .. , Sm} valued coins. The order of coins doesn’t matter. 
# For example, for N = 4 and S = {1,2,3}, there are four solutions: {1,1,1,1},{1,1,2},{2,2},{1,3}. So output should be 4. For N = 10 and S = {2, 5, 3, 6}, there are five solutions: {2,2,2,2,2}, {2,2,3,3}, {2,2,6}, {2,3,5} and {5,5}. So the output should be 5.


# Dynamic Programming Python implementation of Coin  
# Change problem 
def count(S, m, n): 
    table = [[0 for x in range(m)] for x in range(n+1)] 
  
    # Fill the entries for 0 value case (n = 0) 
    for i in range(m): 
        table[0][i] = 1
  
    # Fill rest of the table entries in bottom up manner 
    for i in range(1, n+1): 
        for j in range(m): 
  
            # Count of solutions including S[j] 
            x = table[i - S[j]][j] if i-S[j] >= 0 else 0
  
            # Count of solutions excluding S[j] 
            y = table[i][j-1] if j >= 1 else 0
  
            # total count 
            table[i][j] = x + y 
    print(table)
    return table[n][m-1] 

arr = [1, 2, 3] 
m = len(arr) 
n = 4
print(count(arr, m, n))