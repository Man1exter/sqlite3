import sqlite3

databaseX = sqlite3.connect("itemadd.db")  # connect / create base -> first itemadd.db
cursor = databaseX.cursor() # navigating the database

cursor.execute('''  
               
  insert into results(id,name,surname,score)values(1,"Mariusz","Perzyk",22)  
           
 ''')

# add item to database ID = 1 , NAME = MARIUSZ, SURNAME = PERZYK, SCORE = 22

databaseX.commit()  # save changes to database
databaseX.close() # close database