sname = open("/home/suhair/PycharmProjects/LumPy/File i&o/students")
snset=set()
for item in sname:
    snset.add(item.rstrip("\n"))
print(snset)

sfail = open("/home/suhair/PycharmProjects/LumPy/File i&o/failed")
sfset=set()
for item in sfail:
    sfset.add(item.rstrip("\n"))
print(sfset)

spset = snset-sfset
print(spset)
spass = open("/home/suhair/PycharmProjects/LumPy/File i&o/passed","w")
for item in spset:
    spass.write(item+"\n")