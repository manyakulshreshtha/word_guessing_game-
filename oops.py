string= input("enter string: ")
character=input("enter char: ")
vowel=0
for ch in string:
    if ch ==character:
        pos=str(string.find(ch)+1)
        print("found "+ch+" at "+pos)   
        break
