print ("\n\n#~ Hello this is my min & max finder. ")

nlist = [25,45,85,8,91,99,45,21,13,11,14,65,54,22]

print (f"\n#~ This is your number list :: {nlist}\n\n")

min = max = nlist[0]

for x in nlist:
    if x>max:
        max=x
    if x<min:
        min=x

print (f"# MAX : {max}")
print (f"# MIN : {min}")