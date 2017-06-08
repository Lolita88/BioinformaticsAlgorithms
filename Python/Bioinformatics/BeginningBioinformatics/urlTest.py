import urllib2

response0 = urllib2.urlopen('http://bioinformaticsalgorithms.com/data/challengedatasets/DosR.txt')
pageData1 = str(response0.read())
response0.close()
print(pageData1)


# req = urllib2.Request('http://bioinformaticsalgorithms.com/data/challengedatasets/DosR.txt')
# with urllib2.urlopen(req) as response:
#     pageData = str(response.read())

# pageDataFormatted = pageData.replace('\\r\\n', '\r\n')
# print(pageDataFormatted)


#import from local file
#DosR = open('DosR.txt').read()