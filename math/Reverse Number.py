num = int(input())
value = 0 
while (num > 0):
    value = value * 10 
    value += num % 10
    num = num // 10 

print(value)
