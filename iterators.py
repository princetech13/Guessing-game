mytuple = ("apple","banana","cherry")

i = 0
while i < len(mytuple):
    print(mytuple[i])
    i = i + 1
for x in mytuple:
    print(x)
myit = iter(mytuple)
print(next(myit))
print(next(myit))
print(next(myit))

class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        x = self.a
        self.a +=1
        return x

