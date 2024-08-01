#Step 0 - import sqlite3
import sqlite3
import queries as q
# Step 1 - Connect to the database 

connection = sqlite3.connect('rpg_db.sqlite3')

# Step 2 - Create the cursor

cursor = connection.cursor()

# Step 3 - Write the Query
# (See the queries.py file)

# Step 4 - Execute the query and get the results 

results = cursor.execute(q.SELECT_ALL).fetchall()

if __name__ == '__main__':
    print(results[:5])