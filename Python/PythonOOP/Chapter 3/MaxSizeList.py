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