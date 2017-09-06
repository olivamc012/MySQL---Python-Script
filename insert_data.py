#import connector
print "Using MySQLdb…"
import MySQLdb
#createconnection
myConnection = MySQLdb.connect( host = "testinstance.cuprnqmjai1h.us-east-2.rds.amazonaws.com",
                                user = "testuser",
                                passwd = "*****",
                                db = "masterdb" )

#create cursor
cursor = myConnection.cursor()

#dictionary of customer info
data_customer = {
                'first_name': 'Matt',
                'last_name' : 'Oliva',
                'email': 'olivamc012@gmail.com',
}

#insertion of customer info
add_customer = ("insert into customer_info "
                "(first_name, last_name, email)"
                "values (%(first_name)s,%(last_name)s,%(email)s)")

#execute the fucntion
cursor.execute(add_customer, data_customer)

print('one row inserted')
print(cursor.rowcount)

#commit
myConnection.commit()
cursor.close()
myConnection.close()
