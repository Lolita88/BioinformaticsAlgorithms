from WriteFile import WriteFile

class DelimFile(WriteFile):
    #):  its instance writes values separated by a delimeter:   
    #a,b,c,d

    def __init__(self, filename, delimiter):
        #have to pass filename to super init
        super(DelimFile,self).__init__(filename)
        self.myDelim = delimiter
        
    def write(self, myList):
        for i in range (len(myList)):
            if myList[i].find(self.myDelim) == True:
                #print "need quotes"
                myList[i] = '"' + myList[i] + '"'

        myText = self.myDelim.join(myList)
        self.writeOutput(myText) #passes formatted string with delimiter
    