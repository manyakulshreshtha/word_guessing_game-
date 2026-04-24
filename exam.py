import string
fhand=open("test.txt")
count=dict()
for line in fhand:
    line = line.translate(line.maketrans("", "", string.punctuation))
    line.lower()
    words=line.split()
    for word in words:
        if word in count:
            count[word]+=1
        else:
            count[word]=1
print(count)
