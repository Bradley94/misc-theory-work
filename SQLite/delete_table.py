import sqlite3

# Create a connection to our database, in the brackets if db doesn't exist it creates it
conn = sqlite3.connect('customer.db') 

# Create a cursor (tells the db what to do)
c = conn.cursor()

# Drop table - will be gone until recreated manually again (PERMANENT DELETION!)
c.execute("DROP TABLE customers")
conn.commit()

# Query the database 	
c.execute("SELECT rowid, * FROM customers")

items = c.fetchall()

for item in items:
	print(item)
	

print("Command executed succesfully...") # optional print for when calling the code
# Commit our command
conn.commit()

# Close our connection
conn.close()
