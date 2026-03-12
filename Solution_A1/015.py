name = input()
sname = input()
age = input()

if len(name) > 5 and len(sname) > 5:
    password = name[:2] + sname[-1] + age[-1]
else:
    password = name[0] + age + sname[-1]

print(password)