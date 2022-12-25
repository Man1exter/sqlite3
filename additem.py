import sqlite3

database = sqlite3.connect("base.db")  # connect / create base -> first firstbase.db
cursor = database.cursor() # navigating the database

cursor.execute('''  
               
  INSERT INTO scores(
      id,name,surname,result)values(
          1,"Mario","Perk",22)  
           
  ''')

# add item to database ID = 1 , NAME = MARIUSZ, SURNAME = PERZYK, SCORE = 22

database.commit()  # save changes to database
database.close() # close database