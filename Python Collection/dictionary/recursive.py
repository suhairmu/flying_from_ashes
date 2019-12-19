sample = "ABABA"
dict={}
for var in sample:
    if (var not in dict):
        dict[var]=1
    else:
        print("recursive character is", var)
        break