# MySQL---Python-Script

#import connector
print "Using MySQLdb…"
import MySQLdb
#create connection
myConnection = MySQLdb.connect( host = "testinstance.cuprnqmjai1h.us-east-2.rds.amazonaws.com", user = "testuser", passwd = "testuser1", db = "masterdb" )

#create cursor
cursor = myConnection.cursor()

#create table
cursor.execute("create table file_names(id int(11) NOT NULL AUTO_INCREMENT, first_name varchar(255) NOT NULL, last_name varchar(255) NOT NULL, email varchar(255) NOT NULL, PRIMARY KEY (id))")

print("table printed successfully")
cursor.close()
myConnection.close()
