import sqlite3

# Create a connection to our database, in the brackets if db doesn't exist it creates it
conn = sqlite3.connect('customer.db') 

# Create a cursor (tells the db what to do)
c = conn.cursor()

# Create a table
# Why we use multi-line instead of having it all on one line (READABILITY!)
# c.execute("CREATE TABLE customers (first_name DATATYPE, last_name DATATYPE, email DATATYPE)")

c.execute("""CREATE TABLE customers (
		first_name text,
		last_name text,
		email text
	)""")

# NULL - bool - exists or not 
# INTEGER - whole number 
# REAL - decimals 
# TEXT - string
# BLOB - stored as is e.g. image, mp3 file 

# Commit our command
conn.commit()

# Close our connection
conn.close()
