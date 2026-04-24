sum=0
for i in range(2,20000):
    for num in range(2,int(i**0.5)+1):
        if i%num==0:
            break
        else:
            sum+=i
print(sum)