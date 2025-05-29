get = int(input('Enter your Number :- '))

res = 0 
while  get > 0:
   get = get // 10
   res += 1 
   print(get)


print(res)
