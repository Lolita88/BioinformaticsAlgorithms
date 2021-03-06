import os.path
import pickle

class ConfigKeyError(Exception):
    
    def __init__(self, this, key):
        
        self.key = key
        self.keys = this.keys()
        
    def __str__(self): 
        # str method gets called when exception is raised
        return 'key "{0}" not found. Available keys: ({1})'.format(self.key, ', '.join(self.keys))

class ConfigDict(dict):
    # will need to write an empty dict to the file, pickle will fail if try to read an empty file
    # dump obj to file if file doesn't exist

    config_directory = '/home/llannon/configs/'

    # config_name is name of a pickle file inside of configs dir
    def __init__(self, config_name):
        
        # set name of file in private instance (_private)
        self._filename = config_name 
        # if file doesn't exist
        if not os.path.isfile(self._filename):
            try:
                open(self._filename, 'w').closed()
            except IOError:
                raise IOError('arg must be valid path')
            # for each line in the file
        with open(self._filename) as fh:
            # use pickle load intstead
            unpickledObj = pickle.load(fh)
            #for line in fh:
                # strip the line, (calling rstrip on the line to remove whitespace)
                #line = line.rstrip()
                # split the line on a '=', returns key, value
                #key, value = line.split('=', 1)
                # set the key and value in the instance:
                #parent class version
                dict.__setitem__(self, key, value)

    def __setitem__(self, key, value):
        
        # (called when user says thisdict[key] = value)
        # set key, value in isinstance
        # (remember, don't use self[key] = value!)
        # instead, call the dict() constructor -- as was done in __init__
        dict.__setitem__(self, key, value)
        # open the file (use the name you stored in instance)
        with open(self._filename, 'w') as fh:
            #just use pickle dump to store the item in the file
            picke.dump(self, fh)
        # loop through the instance's key / value pairs
            #for key, val in self.items():
            # write each key/value on a line, join by an equal's sign
                #fh.write('{0}={1}\n'.format(key, val))
        
    def __getitem__(self, key):
        
        if not key in self:
            raise ConfigKeyError(self, key)
        return dict.__getitem__(self, key)

#cc = ConfigDict('config.txt')

#cc['sql_query'] = 'SELECT this FROM that WHERE condition'
#cc['email_to'] = 'me@mydomain.com'
#cc['num_retries'] = '5'

