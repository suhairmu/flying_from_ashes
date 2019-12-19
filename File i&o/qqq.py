# val = 20
# def demo():
#     val = 10
#     print(val*20)   #200
# print(val)  #20
# demo()


val = 20
def demo():
    global val
    val = 10
    print(val*20)   #200
demo()
print(val)  #20