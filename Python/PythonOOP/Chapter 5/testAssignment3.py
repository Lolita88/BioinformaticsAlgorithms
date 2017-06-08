import sys
from Assignment3 import ConfigDict

cd = ConfigDict('config_file.txt')

for arg in sys.argv:
    print arg
print len(sys.argv)

if len(sys.argv) == 3:
    key = sys.argv[1]
    value = sys.argv[2]
    print('writing data:  {0}, {1}'.format(key, value))

    cd[key] = value

else:
    print('reading data:py')
    for key in cd.keys():
        print('  {0} = {1}'.format(key, cd[key]))
        





