import abc

class WriteFile(object):
    #the parent class to both LogFile and DelimFile
    __metaclass__ = abc.ABCMeta

    def __init__(self, filename):
        self.myFilename = filename

    def writeOutput(self, text):
        print text 
        myText = text
        fh = open(self.myFilename, 'w')
        fh.write(text)
        fh.close()

    @abc.abstractmethod    
    def write(self):
        return