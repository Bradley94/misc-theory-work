import sqlite3

# Create a connection to our database, in the brackets if db doesn't exist it creates it
conn = sqlite3.connect('customer.db') 

# Create a cursor (tells the db what to do)
c = conn.cursor()

# Query the database
c.execute("SELECT * FROM customers")
#print(c.fetchone()[0])
#print(c.fetchmany(3))

items = c.fetchall()

print("NAME " + "\t\tEMAIL")
print("--------" + "\t--------")
for item in items:
	#print(item)
	#print(item[0])
	print(item[0] + " " + item[1] + "\t" + item[2])

print("Command executed succesfully...") # optional print for when calling the code
# Commit our command
conn.commit()

# Close our connection
conn.close()
