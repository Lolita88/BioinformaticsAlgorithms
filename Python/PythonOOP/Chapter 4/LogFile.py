from datetime import datetime
from WriteFile import WriteFile

class LogFile(WriteFile):
    #its instance writes a date and message to a log file:  
    #2015-01-21 18:35   this is a log message
    #def __init__(self, filename): don't need
    def write(self, myString):
        dt = datetime.now()
        dt_str = dt.strftime('%Y-%m-%d %H:%M')
        self.writeOutput(dt_str + " " + myString)
        