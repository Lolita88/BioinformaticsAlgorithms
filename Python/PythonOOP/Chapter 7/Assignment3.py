import os
import pickle

class ConfigKeyError(Exception):
    
    def __init__(self, this, key):
        
        self.key = key
        self.keys = this.keys()
        
    def __str__(self): 
        # str method gets called when exception is raised
        return 'key "{0}" not found. Available keys: ({1})'.format(self.key, ', '.join(self.keys))

class ConfigPickleDict(dict):
    
    config_dir = '/Users/lauralannon/Documents/configs/'
    # will need to write an empty dict to the file, pickle will fail if try to read an empty file
    # dump obj to file if file doesn't exist

    # config_name is name of a pickle file inside of configs dir
    def __init__(self, picklename):
        self._filename = os.path.join(ConfigPickleDict.config_dir, picklename + '.pickle')
        # if file doesn't exist
        if not os.path.isfile(self._filename):
            with open(self._filename, 'wb') as fh:
                pickle.dump({}, fh)
        with open(self._filename) as fh:
            unpickledObj = pickle.load(fh)
            # update is a dict method
            self.update(unpickledObj)

    def __setitem__(self, key, value):
        dict.__setitem__(self, key, value)
        # open the file (use the name you stored in instance)
        with open(self._filename, 'wb') as fh:
            #just use pickle dump to store the item in the file
            pickle.dump(self, fh)  
        
    def __getitem__(self, key): 
        if not key in self:
            raise ConfigKeyError(self, key)
        return dict.__getitem__(self, key)


