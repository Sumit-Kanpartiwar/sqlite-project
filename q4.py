"""   q4 = create a tuple set of all the records avaialble in all the five file and then store it in sqllite DB . 
    (aah,>=,354,fdsf,wer)"""

import csv
obj=count()
file1='vocab.enron.txt'
file2='vocab.kos.txt'
file3='vocab.nytimes.txt'
file4='vocab.pubmed.txt'
list_1=obj.file_to_list(file1)
list_2=obj.file_to_list(file2)
list_3=obj.file_to_list(file3)
list_4=obj.file_to_list(file4)

import sqlite3
db=sqlite3.connect('database.db')
c=db.cursor()
c.execute("create table data(enron blob,kos blob, nytimes blob, pubmed blob)")

for x,y,z,a in zip(list_1,list_2,list_3,list_4):
    t=(x,y,z,a)
    c.execute("INSERT INTO data(enron, kos, nytimes, pubmed) VALUES ( ?, ?, ?, ?);",t) 
    
for i in c.execute("select * from data"):
    print(i)
