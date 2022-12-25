import sqlite3

database = sqlite3.connect("firstbase.db")  # connect / create base -> first base.db
cursor = database.cursor() # navigating the database

cursor.execute('''  
               
  CREATE TABLE scores(           
     id integer,
     name string,           
     surname string)    
           
 ''')  # select questions to database , # scores - table

database.commit()  # save changes to database
database.close()   # close database