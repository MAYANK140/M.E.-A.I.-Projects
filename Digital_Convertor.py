def convertor(base, n):
    sum = 0
    i = 0
    while n != 0:
        rm = n%10
        sum += rm * base**i
        n //= 10
        i+=1
    return sum
result = convertor(16, 11)
print(result)
