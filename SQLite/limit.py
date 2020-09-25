import sqlite3

# Create a connection to our database, in the brackets if db doesn't exist it creates it
conn = sqlite3.connect('customer.db') 

# Create a cursor (tells the db what to do)
c = conn.cursor()


# Query the database - ORDER BY 								     
c.execute("SELECT rowid, * FROM customers ORDER BY rowid DESC LIMIT 2")

items = c.fetchall()

for item in items:
	print(item)
	

print("Command executed succesfully...") # optional print for when calling the code
# Commit our command
conn.commit()

# Close our connection
conn.close()
