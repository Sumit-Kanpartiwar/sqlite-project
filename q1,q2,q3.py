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
