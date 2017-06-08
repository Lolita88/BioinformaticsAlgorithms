class MaxSizeList(object):
    def __init__(self, size):
        self.maxSize = size
        self.myList = []
        
    def set_list(self, aVar):
        self.myList.append(aVar)
        while(len(self.myList) > self.maxSize):
            self.myList.pop(0)
    def get_list(self):
        #while(len(self.myList) > self.maxSize):
            #self.myList.pop(0)
        return self.myList
    def push(self, myVar):
        #self.myList.append(myVar)
        self.set_list(myVar)


a = MaxSizeList(3)
b = MaxSizeList(1)

a.push("hey")
a.push("hi")
a.push("let's")
a.push("go")

b.push("hey")
b.push("hi")
b.push("let's")
b.push("go")

print(a.get_list())
print(b.get_list())
