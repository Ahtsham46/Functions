def sum_n(n):
    if n == 0:
        return 0
    return sum_n(n-1)+n   
sum = sum_n(7)
print(sum)