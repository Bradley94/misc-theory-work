import sqlite3

# Create a connection to our database, in the brackets if db doesn't exist it creates it
conn = sqlite3.connect('customer.db') 

# Create a cursor (tells the db what to do)
c = conn.cursor()

many_customers = [
					('Wes', 'Brown', 'wes@brown.com'),
					('Steph', 'Kuewa', 'steph@kuewa.com'),
					('Dan', 'Pas', 'dan@pas.com'),
				 ]

c.executemany("INSERT INTO customers VALUES (?,?,?)", many_customers) # ? = placeholder for sqlite3





print("Command executed succesfully...") # optional print for when calling the code
# Commit our command
conn.commit()

# Close our connection
conn.close()
