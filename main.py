import psycopg2
from queries import \
    read_all_query, create_row_query, update_rows_query, delete_rows_query

con = psycopg2.connect(
    user='postgres',
    password='admin',
    host='127.0.0.1',
    port='5432',
    database='postgres'
)
cur = con.cursor()
cur.execute(
    #Call one of those functions we wrote:
    #read_all_query, create_row_query, update_rows_query, delete_rows_query
)
#Use this to see the data if you select read_all_query
#print(cur.fetchall())
con.commit()
cur.close()
con.close()