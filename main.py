﻿# -*- coding: utf-8 -*-

"""
created by Réchèr. Licence CC-BY or Free Art License.
https://github.com/darkrecher/Word-Filter
send me some bitcoins if you like my spirit and/or my body : 12wF4PWLeVAoaU1ozD1cnQprSiKr6dYW1G
"""

import os
from string import maketrans
from wrdstock import WordStocker
from wrdfinder import WordFinder
from bnchread import BunchReader


TRANSLATION_TABLE = maketrans("0123456789", " " * 10)
INPUT_FILE_NAME = "input.txt"
INTERMEDIATE_FILE_NAME_MIXED = "interm-mixed.txt"
INTERMEDIATE_FILE_NAME_UPPER = "interm-upper.txt"
INTERMEDIATE_FILE_NAME_TITLE = "interm-title.txt"
OUTPUT_FILE_NAME = "output.txt"
DICTIONARY_FILE_NAME = "dictionary.txt"

# TODO : use logging.
def log(*list_msg):
    """ OK, I just do a print. Sorry. """
    for elem in list_msg:
        print elem,
    print ""

def split_on_numbers(str_source):
    return str_source.translate(TRANSLATION_TABLE).split()

def process_one_data_elem(data_elem, word_finder):
    list_w_mixed_case_of_elem = []
    list_w_upper_case_of_elem = []
    list_w_title_case_of_elem = []
    list_w_all_of_elem = []
    list_fragment = split_on_numbers(data_elem)
    for fragment in list_fragment:
        list_w_all_of_elem.extend(word_finder.find_all_words(fragment))
    for word_to_add in list_w_all_of_elem:
        if word_to_add.upper() == word_to_add:
            list_w_upper_case_of_elem.append(word_to_add)
        elif word_to_add.title() == word_to_add:
            list_w_title_case_of_elem.append(word_to_add)
        else:
            list_w_mixed_case_of_elem.append(word_to_add)
    tuple_lists_w_of_elem = (
        list_w_mixed_case_of_elem,
        list_w_upper_case_of_elem,
        list_w_title_case_of_elem)
    return tuple_lists_w_of_elem
    
def write_unique_words(interm_file_name, file_output, task_index):
    interm_file_size = os.path.getsize(interm_file_name)
    file_interm = open(interm_file_name, "rb")
    list_unique_word = []
    log_period = 2000
    nb_word_written = 0
    for interm_word in file_interm.xreadlines():
        if interm_word not in list_unique_word:
            list_unique_word.append(interm_word)
            file_output.write(interm_word)
            nb_word_written += 1
        log_period -= 1
        if log_period == 0:
            nb_bytes_to_read = interm_file_size - file_interm.tell()
            log(str(task_index), "/5 ", str(nb_bytes_to_read))
            log_period = 2000
    file_interm.close()
    return nb_word_written
    
def main_function():

    input_reader = BunchReader(INPUT_FILE_NAME)
    if not input_reader.is_valid:
        return
    
    log("Reading dictionary of English words.")
    # TODO : all that dictionary reading stuff should go in a specific class
    dictionary_file_size = os.path.getsize(DICTIONARY_FILE_NAME)
    nb_bytes_to_read = dictionary_file_size
    log("1/5 ", str(nb_bytes_to_read))
    #nb_bytes_last_logged = nb_bytes_to_read    
    log_period = 20000
    ws_upcase = WordStocker()
    dictionary_file = open(DICTIONARY_FILE_NAME, "rb")
    for dictionary_line in dictionary_file.xreadlines():
        dictionary_word_upped = dictionary_line.strip().upper()
        if len(dictionary_word_upped) >= 4:
            ws_upcase.add_word(dictionary_word_upped)
        log_period -= 1
        if log_period == 0:
            nb_bytes_to_read = dictionary_file_size - dictionary_file.tell()
            #if nb_bytes_last_logged - nb_bytes_to_read >= 10000:
            log("1/5 ", str(nb_bytes_to_read))
            #nb_bytes_last_logged = nb_bytes_to_read            
            log_period = 20000
            
    dictionary_file.close()
    word_finder = WordFinder(ws_upcase)
    log("Finished.")
    
    log("Reading the data file.")
    file_interm_mixed = open(INTERMEDIATE_FILE_NAME_MIXED, "wb")
    file_interm_upper = open(INTERMEDIATE_FILE_NAME_UPPER, "wb")
    file_interm_title = open(INTERMEDIATE_FILE_NAME_TITLE, "wb")
    nb_bytes_to_read = input_reader.file_size
    log("2/5 ", str(nb_bytes_to_read))
    #nb_bytes_last_logged = nb_bytes_to_read
    log_period = 200
    data_elem = input_reader.get_next_data_elem()
    while data_elem is not None:
        tuple_lists_w_of_elem = process_one_data_elem(data_elem, word_finder)
        for word in tuple_lists_w_of_elem[0]:
            file_interm_mixed.write(word + "\n")
        for word in tuple_lists_w_of_elem[1]:
            file_interm_upper.write(word + "\n")
        for word in tuple_lists_w_of_elem[2]:
            file_interm_title.write(word + "\n")        
        data_elem = input_reader.get_next_data_elem()
        log_period -= 1
        if log_period == 0:
            nb_bytes_to_read = input_reader.file_size - input_reader.tell()
            #if nb_bytes_last_logged - nb_bytes_to_read >= 10000:
            log("2/5 ", str(nb_bytes_to_read))
            #nb_bytes_last_logged = nb_bytes_to_read
            log_period = 200
    input_reader.close()
    file_interm_mixed.close()
    file_interm_upper.close()
    file_interm_title.close()
    ws_upcase.trash_stocked_words()
    del ws_upcase
    ws_upcase = None
    log("Finished.")

    log("Re-reading intermediate file, and writing words in output file.")
    file_output = open(OUTPUT_FILE_NAME, "wb")
    nb_w_mixed_case = write_unique_words(
        INTERMEDIATE_FILE_NAME_MIXED, 
        file_output, 
        3)
    nb_w_upper_case = write_unique_words(
        INTERMEDIATE_FILE_NAME_UPPER, 
        file_output, 
        4)
    nb_w_title_case = write_unique_words(
        INTERMEDIATE_FILE_NAME_TITLE, 
        file_output, 
        5)
    file_output.close()
    log("Finished.")

    log(" **** Total words found **** ")
    log(" - mixed case :", str(nb_w_mixed_case))
    log(" - upper case :", str(nb_w_upper_case))
    log(" - title case :", str(nb_w_title_case))    
    log("")
    log(" **** Process completely finished. ****")
    log("")
    log("A file was created in the executable directory :", OUTPUT_FILE_NAME)
    log("")
    raw_input("Press enter to close this window.")

if __name__ == "__main__":        
    main_function()