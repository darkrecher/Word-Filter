# Word Filter #

Extracts words of the English dictionary from a big text file.

This script was created to answer a question on Rugatu

http://www.rugatu.com/questions/12480/find-and-filter-words-in-random-text


# Specifications #

These specs are a copy of the question created on Rugatu, by the user bitcoinfoundation. (http://www.rugatu.com/users/2785/bitcoinfoundation)

I am trying to filter words out of random text. Here an example:

    NTWzd1Y4zMS6xydrhNC9kKub2CpXZCoc9 QoWyBDDKNtYNYx2xAsFgezAyvY7n5tUy 
    7zBD5spS8v5WruYbxgS3FaE5VukokLCj5 7Xaiq8MjG43di8v3wq2t5dwWzk5QBqDcL 
    71wo6gGX8uGWi7RGxJkmtfmVernSX41L3 HYyrdvrwbt4vj5HouSez6Fa3SyC11PBaz 
    AHqt1AGMcZ8CFActorYzJxcxjaCpY BTrUVCssfihZEx1qmYw3K4owfFpuWiYzd 
    CHkowJrmRHZb5afdvTtR4Hp9sYDvyjZiC

As one might see there are some words in the 3th row "HouSe" and in the 4th row "FActorY" this is what I am looking for. Following reqirments :

 - Scann entire text
 - Filter1 all english dictionary words made out of uppercase and lowercase letters which are longer than 3 letters. Example: Don't filter eGg, sEx, ArM but bEef, Look, WaRm etc.
 - Filter2 all english dictionary words made of only uppercase and lowercase letters which are longer than 3 letters. Example: Don't filter EGG, sex, ARM but BEEF, look, warm etc.
 - Filter all english dictionary words start with an uppercase letter and the rest are lowercase letters which are longer than 3 letters. Example: Don't filter Egg, Sex, Arm but Beef, Look, Warm etc.
 - Show all filtered results in a .txt file or in a excel sheet. Ideal "Filtered words 1" space "Filtered words 2" space "Filtered words 3".
 - Must be able to filter millions of rows without problems.
 - Solution should be simple and easy if possible in excel, html, VB.
 - The process needs to be explained properly.


# Answer to the specs #

This chapter is a copy of the answer I made on Rugatu. http://www.rugatu.com/questions/12480/find-and-filter-words-in-random-text/12503.

You get an executable I provide to you. It works on Windows.

The executable needs a .txt file, encoded in ASCII, that contains all the English words. I provide that file too. You will be able to modify it if you want. The dictionary used is the file "sowpods.txt", which I get from that scrabble game : http://sourceforge.net/projects/scrabbledict/

The input file is a text file, encoded in ASCII.

The input file must be put in the same directory than the executable, with a specific name. Each source string is separated by at least one space, or one newline character (\n), or any combinations of the two.

The executable process each source string separately, one after another.

The executable writes an output text file, in the same directory, encoded in ASCII.

The output files contains all the english words that were found in the input file. Each word is separated by a newline. (Having newline will make it easier to reimport it in Excel).

The words found are written in the output file exactly as they were in the input file (same case).

The output file contains, in that order :

 - the mixed-case words
 - the upper-case words
 - the title-case words

There is no further sorting of the words. (no alphabetic, length, ...)

A word found many times in the input file, with the same case, appears only once in the output file.

A word found many times in the input file, with different cases, will appear as many times as different cases. It means that a unique word may appear many times in the case-insensitive part, plus one time in the upper-case part, plus one time in the title case part. (See example below)

Some specific english words may add many words in the output file. For example : "grasshopper" will add the words "grass", "hopper" and "grasshopper".

The executable sends some information on the standard output, to tell the progress of the whole processing. So that you know approximately how long it will take.

The executable is coded in python, and embeds the python interpretor. (I use the py2exe software to merge my code and the interpretor). It means the execution time will be "quite fast". Though I can not guarantee any time limit.

When the reward for this question is taken (wether I am the winner or not), the code will be released in my github repository, under CC-BY license.

# Example #

## input file ##

    71wo6gGX8uGWi7RGxJkmtfmVernSX41L3 HYyrdvrwbt4vj5HouSez6Fa3SyC11PBaz
    AHqt1AGMcZ8CFActorYzJxcxjaCpY BTrUVCssfiHELLOqmYw3K4owfFpuWiYzd
    BTrUVCssfiqmYwBeer3K4owfFpuWiYzd aaaHELLObbbbBeercccc
    aaadRaGoNbbbdRAGONccccccDragonddddddDRAGONeeeeeeDRAGONffff

## output file ##

    HouSe
    FActorY
    dRaGoN
    dRAGON
    HELLO
    DRAGON
    Beer
    Dragon

(note that HELLO and Beer appear only once in the output file, though they are present twice in the input file)

(Some other words may appear in the output file, because the input data may contain other English words I did not noticed.)


# How to use it #

The input data must be a txt file, in the same directory as the script, and must be named "input.txt". You must replace the example file "input.txt" that was bundled with the script.

Execute the command `python main.py`

A window should open, showing some progress. Each progress information is given with this format :

-current main step- / -total main step-  -quantity of work in current step-

Example : 

    2/5  348755
    2/5  345755
    2/5  343255
    ......

It means you are currently in the step 2, there is a total of 5 steps, and there is "343255" quantity of work left for that step 2. The quantity of work decreases. When it reaches 0, the process goes to the next step.

When finished, the window stays. It asks you to press Enter to close it.

A file named "output.txt" is created in the same directory as the script. If there was an existing "output.txt" file, its content is removed, and replaced by the new content. Make some saves between 2 executions !


# Intermediate files #

If the process crashes during execution (not supposed to happen, but we never know), you can still get a part of the work done, thanks to intermediate files.

The script creates 3 intermediate files, in the same directory, and fills them during the reading of the input file.
 - interm-mixed.txt contains all the mixed-case words already found.
 - interm-upper.txt contains all the upper-case words already found.
 - interm-title.txt contains all the title-case words already found. 

Some duplicate words may appear in these files. 

The final file "output.txt" contains all the words found, with no duplicates.

You should not modify the intermediate files while the process is running.


# Performance #

I tested with an input file of 500 kilobytes, containing 50 000 rows of data. The process took a little more than 1 hour. So, it is not fast, but it will work with millions of datas.


# Converting to a .exe #

It can be done, by using py2exe. Look at the code and docstring of the file `setup.py`, in this repository.


# Conception #

This repository does not contain any conception document, nor does describe how the code is structured. Sorry for the inconvenience. Explore it on your own ! 


# Credits #

created by Réchèr. Licence CC-BY or Free Art License.

https://github.com/darkrecher/Word-Filter

send me some bitcoins if you like my spirit and/or my body : 12wF4PWLeVAoaU1ozD1cnQprSiKr6dYW1G
