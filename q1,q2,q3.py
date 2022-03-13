"""    q1 = try to find out a count of each and every word in a respective file return a list of tuple with word and its respective count 
       sample example -  [('sudh', 6 ) , ('kumar',3)]
    q2 = try to perform a reduce operation to get a count of all the word starting with same alphabet
        sample examle = [(a,56) , (b,34),...........]
    q3 = Try to filter out all the words from dataset . """
import csv
import logging 
logging.basicConfig(filename='task.log',level=logging.DEBUG)
filename='simple.txt'
count_obj=count()
filelist=count_obj.file_to_list(filename)
list_word_count=count_obj.word_count(filelist)
print(list_word_count)
print("\n\n\n\n\n\n")
list_alph_count=count_obj.alph_count(filelist)
print(list_alph_count)
print("\n\n\n\n\n\n")
list_filter_words=count_obj.word_filter(filelist)
print(list_filter_words)
