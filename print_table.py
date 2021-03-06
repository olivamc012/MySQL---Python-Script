print "Using MySQLdb…"
import MySQLdb

myConnection = MySQLdb.connect( host = "testinstance.cuprnqmjai1h.us-east-2.rds.amazonaws.com",
                                user = "testuser",
                                passwd = "*****",
                                db = "masterdb")

cursor = myConnection.cursor()
query = ("SELECT id, first_name, last_name, email FROM customer_info")

#execute SQL select statement
cursor.execute(query)

#iterate over the table and print out data
for (id, first_name, last_name, email) in cursor:
    print("{}, {}, {}, {}".format(id, first_name, last_name, email))

cursor.close()
myConnection.close()
