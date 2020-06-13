myvars = {}
with open("file") as myfile:
    for line in myfile:
        name, var = line.partition("=")[::2]
        myvars[name.strip()] = chr(int(var))
flag = ""
for i in range(36):
    flag += myvars.get("x" + str(i))

print(flag)