def myfunc():
    x = 300
    print(x)
myfunc()


x = 500
def fun():
    global x
    x = "interesting"
fun()
print("python is" " " + x)


x = "aweasome"
def princ():
    x = "favorite"
    print("python is my "  + x)
princ()
print("python is " +  x )

def greeting(name):
    txt = "welcome mr"
    age = 26 
    print(txt + " " "you are now" + str(age) + "years old")
greeting("prince")
