#f=open("/home/suhair/PycharmProjects/LumPy/File i&o/numfile")
#print(f.mode)   #default mode is read

#list = ["abefg"]
ls = ["zxcxv","lkkjh"]
#f=open("text.txt","w")
f=open("text.txt","a")
for item in ls:
    f.write(item+"\n")