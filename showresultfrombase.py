import sqlite3

database = sqlite3.connect("base.db")  # connect / create base -> first base.db
cursor = database.cursor() # navigating the database

cursor.execute('''
        
        select * from scores
        
''')

# select from table -> scores

rows = cursor.fetchall()

for i in rows:
    print("----------------")
    print(i[0],i[1],i[2],i[3])
    print("----------------")
    
# All columns/rows from DataBase


cursor.execute('''
        
        select count (*) from scores
               
''')

rows_get = cursor.fetchall()
print("ROWS:",rows[0])

# Results from table

database.commit()  # save changes to database
database.close() # close database