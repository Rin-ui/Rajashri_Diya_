def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fact(n - 1) * n

f = 5
res = fact(f)
print(res)  # Output: 120
