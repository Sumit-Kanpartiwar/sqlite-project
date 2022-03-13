import csv
import logging 
logging.basicConfig(filename='task.log',level=logging.DEBUG)
class count:        
    try:
        logging.info("defining file to list converter function with filename as input argument")
        def file_to_list(self,filename):
            with open(filename,'r+',encoding='utf-8') as f:
                csvfile=csv.reader(f,delimiter='\n')
                l=[]
                for i in csvfile:
                    l.extend(i)
            return l
    except Exception as e:
        logging.error("an error occured while opening the file and saving data in list")
        logging.info(f"the error is :{e}")  
    
    try:
        logging.info("defining a word counter fuction for filelist to return a tuple of word and its count")
        def word_count(self,filelist):
            ls=[]
            count=0
            for word in filelist:
                if word in ls:
                    continue
                else:
                    ls.append((word,filelist.count(word)))
            return ls
    except Exception as e:
        logging.error("an error occured in word_count() function")
        logging.info(f"the error is :{e}")

    try:
        logging.info("defining a starting alphabet counter fuction to get a list a tuples having count of same starting alphabet in each word")
        def alph_count(self,filelist):
            ls="a b c d e f g h i j k l m o p q r s t u v w x y z".split()
            ns=[]
            for char in ls:
                count=0
                for word in filelist:
                    if word[0]==char: 
                        count=count+1
                ns.append((char,count))
            return ns
    except Exception as e:
        logging.error("an error occured in alph_count() function")
        logging.info(f"the error is :{e}")

    try:
        logging.info("defining a word filter funtion to filter only word from every line in filelist")
        def word_filter(self,filelist):
            ns=[]
            for word in filelist:
                nword=''
                for char in word:
                    if char.isalpha(): 
                        nword+=char
                if len(nword)!=0:
                    ns.append(nword)
            return ns
    except Exception as e:
        logging.error("an error occured in alph_count() function")
        logging.info(f"the error is :{e}")    