import sqlite3
import pandas as pd

# SQLITE connection Variables
conn = sqlite3.connect('buddymove_holidayiq.sqlite3')
curs = conn.cursor()

# Load in the CSV to a Pandas df

df = pd.read_csv('buddymove_holidayiq.csv')

if __name__ == "__main__":
    # Turn dataframe into a table called 'review'
    df.to_sql('review', conn, if_exists='replace')

    # Query the table to ensure that the data was truly added.
    
    # Query 1
    # curs.execute('''SELECT COUNT(*) FROM review;''')
    # print(curs.fetchall())

    # Nature and Shopping both >= 100

    NATURE_SHOPPING = '''
        SELECT COUNT(*) AS greater_100
        FROM review
        WHERE nature >= 100 AND shopping >= 100;
        '''
    
    curs.execute(NATURE_SHOPPING)
    print(curs.fetchall())
