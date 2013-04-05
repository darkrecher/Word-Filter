# -*- coding: utf-8 -*-

"""
created by Réchèr. Licence CC-BY or Free Art License.
https://github.com/darkrecher/Word-Filter
send me some bitcoins if you like my spirit and/or my body : 12wF4PWLeVAoaU1ozD1cnQprSiKr6dYW1G
"""

import os

class BunchReader():

    # TODO : chaotic evil. Put what you want, but NOT A STRING !!
    MUST_READ_ANOTHER_BUNCH = 1

    def __init__(self, path_file, bunch_size=250, split_param=None):
        self.is_valid = False
        self.path_file = path_file
        self.bunch_size = bunch_size
        self.split_param = split_param
        self.buffer = ""
        try:
            self.file_size = os.path.getsize(path_file)
        except OSError:
            # TODO : print crap
            print "The file :", path_file, 
            print "does not exist, or can not be accessed"
            return
        try:
            self.file_to_read = open(path_file, "rb")
        except IOError:
            # TODO : print crap
            print "The file :", path_file, 
            print "does not exist, or can not be accessed"
            return        
        self.is_valid = True

    def tell(self):
        return self.file_to_read.tell()
        
    def close(self):
        self.file_to_read.close()
        
    def get_next_data_elem(self):
        get_result = self._get_next_data_elem_read_bunch_once()
        while get_result == BunchReader.MUST_READ_ANOTHER_BUNCH:
            get_result = self._get_next_data_elem_read_bunch_once()
        return get_result
        
    def _get_next_data_elem_read_bunch_once(self):
        buffer_split = self.buffer.split(self.split_param, 1)
        if len(buffer_split) == 2:
            self.buffer = buffer_split[1]
            return buffer_split[0]
        elif len(buffer_split) == 1:
            bunch = self.file_to_read.read(self.bunch_size)
            self.buffer += bunch
            buffer_split = self.buffer.split(self.split_param, 1)
            if len(buffer_split) == 2:
                self.buffer = buffer_split[1]
            else:
                self.buffer = ""
            return buffer_split[0]
        else:
            bunch = self.file_to_read.read(self.bunch_size)
            if bunch == "":
                # end of file, and no more buffer
                return None
            self.buffer += bunch
            return BunchReader.MUST_READ_ANOTHER_BUNCH
        
        