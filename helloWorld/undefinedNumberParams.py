def summNumbers (*numbers):
    res = 0
    for x in numbers:
        res += x
    return res

print(summNumbers(2,5,6))
print(summNumbers(2,5,6,7))