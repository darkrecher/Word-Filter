# -*- coding: utf-8 -*-

"""
created by Réchèr. Licence CC-BY or Free Art License.
https://github.com/darkrecher/Word-Filter
send me some bitcoins if you like my spirit and/or my body : 12wF4PWLeVAoaU1ozD1cnQprSiKr6dYW1G
"""

from wrdstock import WordStocker
    

class WordFinder():

    def __init__(self, ws_upcase):
        self.ws_upcase = ws_upcase
        
    def find_all_words(self, fragment):
        list_all_words = []
        fragment_upped = fragment.upper()
        list_word_pos = self.ws_upcase.list_words_contained_in(fragment_upped)
        for word, pos in list_word_pos:
            pos_word_start = pos
            pos_word_end = pos + len(word)
            word_orig_case = fragment[pos_word_start:pos_word_end]
            list_all_words.append(word_orig_case)
            word_upped = word.upper()
            pos_next_word = fragment_upped.find(
                word_upped, 
                pos_word_start+1)
            while pos_next_word != -1:
                # TODO : crappy and not DRY code.
                pos_word_start = pos_next_word
                pos_word_end = pos_next_word + len(word)
                word_orig_case = fragment[pos_word_start:pos_word_end]
                list_all_words.append(word_orig_case)
                pos_next_word = fragment_upped.find(
                    word_upped, 
                    pos_word_start+1)
        return list_all_words    
    

if __name__ == "__main__":

    ws_upcase = WordStocker()
    ws_upcase.add_word("BEER")
    ws_upcase.add_word("DWARF")
    word_finder = WordFinder(ws_upcase)
    # TODO : add the asserts
    print word_finder.find_all_words("pPpPBERkKkK")    
    print word_finder.find_all_words("pPpPbEeRkKkK")
    print word_finder.find_all_words("pPpPBeerkKkK")
    print word_finder.find_all_words("aadWArfuieauiepPpPBEERkKkK")
    print word_finder.find_all_words("aadWArfuieauiepPpPBEERkKkKaadWArfuieauiepPpPbeerkKkK")
    