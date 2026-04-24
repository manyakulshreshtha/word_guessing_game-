import time 
n=int(input("enter your time: "))
for count in reversed(range(0,n)):
    seconds=count%60
    minu=int(count/60)%60
    hour=int(count/3600)
    print(f"{hour:02}:{minu:02}:{seconds:02}")
    time.sleep(0.1)
print("times! up ")