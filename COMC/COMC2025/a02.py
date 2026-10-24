count = 0
for i in range(10,99):
    if (i//10 > i%10):
        print(i)
        count = count + 1
for i in range(100,500):
    if (i//100 > ((i%100)//10)) and ((i%100)//10 > (i%100)%10):
        print(i)
        count = count + 1
print("count=",count)