import numpy as np

n = 20
k = 3
matrix = np.zeros((n+1,k))
res = 0
c = [7, 3, 5]
summation = 0
diff = 0
prevdiff = 0
print("COSTS = " + str(c))

print("\nSOLUTION n^2 * k")
for i in range(k-1, -1, -1):
    for p in range(0, n+1):
        ex_val = 0
        for j in range(0, n+1):
            if j < p:
                if i == k-1: ex_val += p/(n+1)
                else: ex_val += (matrix[p][i+1])/(n+1)
            else:
                if i == k-1: ex_val += j/(n+1)
                else: ex_val += (matrix[j][i+1])/(n+1)
        ex_val -= c[i]
        matrix[p][i] = max(p, ex_val)
print(matrix)

print("\n SOLUTION n * k")
for i in range(k-1, -1, -1):
    s = summation/(n+1)
    summation = 0
    diff = 0
    prevdiff = 0
    for p in range(0, n+1):
        ex_val = 0
        if i == k-1:
            ex_val = (p**2 + (((n*(n+1))/2) - ((p*(p-1))/2)))/(n+1)
            #else: ex_val = matrix[p-1][i] + (p/(n+1)) + c[i]
        else:
            if p == 0: ex_val = s
            else:
                diff = (matrix[p][i+1]-matrix[p-1][i+1])*p + prevdiff
                prevdiff = diff
                ex_val = s + (diff/(n+1))
        ex_val -= c[i]
        matrix[p][i] = max(p, ex_val)
        summation += matrix[p][i]
print(matrix)
