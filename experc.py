import sqlite3

database = sqlite3.connect("base.db")  # connect / create base -> first base.db
cursor = database.cursor() # navigating the database

cursor.execute('''  
               
  CREATE TABLE scores (           
      id integer,
      name string,           
      surname string,
      result integer)    
           
''')  # select questions to database , # scores - table

database.commit()  # save changes to database
database.close()   # close database