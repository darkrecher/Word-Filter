# -*- coding: utf-8 -*-

"""
created by Réchèr. Licence CC-BY or Free Art License.
https://github.com/darkrecher/Word-Filter
send me some bitcoins if you like my spirit and/or my body : 12wF4PWLeVAoaU1ozD1cnQprSiKr6dYW1G
"""

class WordStocker():

    def __init__(self, word_stocker_to_clone=None, func_change_word=None):
        self._init_with_nothing()
        if word_stocker_to_clone is not None and func_change_word is not None:
            self._init_by_cloning(word_stocker_to_clone, func_change_word)
        
    def add_word(self, word_new):
        len_w_new = len(word_new)
        list_w = self.dict_word_by_len.get(len_w_new)
        if list_w is None:
            self.dict_word_by_len[len_w_new] = [ word_new ]
            self.len_word_min = min(self.len_word_min, len_w_new)
        else:
            # We do not check if the word already exists in the list.
            # We trust the dictionary we have.
            list_w.append(word_new)
            self.dict_word_by_len[len_w_new] = list_w
    
    def list_words_contained_in(self, string_data):
        """
        Tests if any of the word of the whole dictionary is contained in the 
        string_data. (Case sensitive).
        Returns a list of tuple : 
         - Word found in the string_data.
         - Position.
        A word may be many times in string_data. But it will appear only once
        in output list (first one found).
        
        :Example:
        
            >>> ws = WordStocker()
            >>> ws.add_word("BEER")
            >>> ws.add_word("DWARF")
            >>> ws.has_word_contained_in("abcDWARFdefBEERxyz")
            [ ("BEER", 11), ("DWARF", 3) ]
            >>> ws.has_word_contained_in("blarg")
            []
        """
        list_word_pos = []
        for len_w in xrange(self.len_word_min, len(string_data)+1):
            list_w = self.dict_word_by_len.get(len_w)
            if list_w is not None:
                for word in list_w:
                    pos = string_data.find(word)
                    if pos != -1:
                        list_word_pos.append( (word, pos) )
        return list_word_pos
        
    def _init_with_nothing(self):
        self.dict_word_by_len = {}
        # TODO : this is crap, but this works.
        self.len_word_min = 999
        
    def _init_by_cloning(self, word_stocker_to_clone, func_change_word):
        """ this function is useless. Merci au revoir. """ 
        for len_w, list_w in word_stocker_to_clone.dict_word_by_len.items():
            list_w_transformed = [ 
                func_change_word(word_source) 
                for word_source in list_w ]
            self.dict_word_by_len[len_w] = list_w_transformed
            self.len_word_min = min(self.len_word_min, len_w)
            
    def trash_stocked_words(self):
        del self.dict_word_by_len
        self.dict_word_by_len = {}
            
if __name__ == "__main__":
    ws = WordStocker()
    ws.add_word("BEER")
    ws.add_word("DWARF")
    word_found = ws.list_words_contained_in("abcDWARFdefBEERxyDWARFz")
    print word_found
    assert word_found == [ ("BEER", 11), ("DWARF", 3) ]
    word_found = ws.list_words_contained_in("blarg")
    print word_found
    assert word_found == []
    print "unitary test finished"
    
            
            