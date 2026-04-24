myDict = {'Kavi': 10, 'Rajnish': 9, 'Aanjeev': 15, 'Yash': 2, 'Suraj': 32}
keyval=list(myDict.keys())
keyval.sort()
sortdi=dict()
for i in keyval:
    print(i,":",myDict[i])
    sortdi[i]=myDict[i]
print(sortdi)
