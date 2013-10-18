import MySQLdb

def connect():
	try:
		db = MySQLdb.connect(host="dursley.socs.uoguelph.ca",
	            user="drobin03", # replace with your username
        	    passwd="0700662", # replace with your password (student id number, including leading 0)
        	    db="cis3210") # course database
		#db = MySQLdb.connect(host="localhost",
		#	user="root",
		#	passwd="45bananas",
		#	db='cis3210')
	except:
		return None
	return db

def disconnect(db):
	db.close()
