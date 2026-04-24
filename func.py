birthdays = {
"Alice": "1995-05-10",
"Bob": "2000-07-21",
"Charlie": "1998-12-05",
"Diana": "1993-03-15"
}
print("welcome to birthday finder!",','.join(birthdays.keys()))
name=input("enter name:")
name.strip()
if name in birthdays:
    birthdate=birthdays[name]
    year,month,day=birthdate.split('-')
    arranged='/'.join([day,month,year])
    print("the birthdate of ",name," is ",arranged)
else:
    print("name not found")