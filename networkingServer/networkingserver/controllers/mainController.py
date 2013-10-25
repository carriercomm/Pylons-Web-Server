import logging
import json
import MySQLdb
import database
import collections
import signal

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from networkingserver.lib.base import BaseController, render

log = logging.getLogger(__name__)


users = [{'userid': 'fox', 'image': '/img/fox.gif'}, {'userid': 'peppy', 'image': '/img/peppy.gif'}]
message = ""


# initialize connection with the database
db = database.connect()

class MaincontrollerController(BaseController):
    def index(self):
	global users;
	global message
	c.users = users;
	c.message = message
        # Return a rendered template
        #return render('/login.mako')
        # or, return a response
	if (request.method == 'GET'):
		#check if user has logged in already	
		print request.cookies.get( "authenticated" )
		if (request.cookies.get( "authenticated" )):
			return render('/index.mako')
		else:
			return render('/index.mako')
	else:
		return request.method;
    def login(self):
	global db
	if 'username' in request.params and 'password' in request.params:
		uname = request.params['username']
		passwd = request.params['password']

	# Check if username and password tuple exist in DB
	cursor = db.cursor()
	cursor.execute("""
			SELECT username, password
				FROM users
				WHERE username = %s
				AND BINARY password = %s""", (uname, passwd))
	result = cursor.fetchone()
	if result == None:
		return "Invalid"
	else:
		#set a cookie
		response.set_cookie( "authenticated" , uname, max_age=180*24*3600 )
		return "Valid"
    def logout(self):
	response.delete_cookie('authenticated')

    def dashboard(self, username):
	global users
	global message
	c.users = users
	c.message = message
	c.username = username
	return render('/dashboard.mako')

    def userList(self):
	global users
	global message
	global db
	c.users = users
	c.message = message
	if 'username' in request.params and 'password' in request.params:
		uname = request.params['username']
		passwd = request.params['password']

	if (request.method == 'GET'):
		# list all users
		userlist = []	
		if db == None:
			return None
		try:
			cursor = db.cursor()
			cursor.execute("""SELECT userid, username, password FROM users""")
			result = cursor.fetchall()

			for row in result:
				user = {"userid": row[0], "username": row[1], "password": row[2]}
				userlist.append(user)

			cursor.close()
			return json.dumps(userlist)
		except:
			return None
	if (request.method == 'POST'):
		# Add user
		c.username = uname
		c.password = passwd
		
		if db == None:
			return "Connection to the database failed. Please make sure you are connected to the internet."
		cursor = db.cursor()
		cursor.execute("""SELECT MAX(userid) FROM users""")
		userid = int(cursor.fetchall()[0][0])
		userid = userid + 1
		try:		
			cursor.execute("""INSERT into users VALUES(%s, %s, %s)""", (userid, uname, passwd))
			db.commit()
			c.message = ("Successfully added ", (uname))
		except:
			c.message = "Failed to add user %s, that user already exists", (uname)
		
		cursor.close()
		return c.message;

    def users(self, userid):
	global users
	global message
	global db
	c.users = users
	c.message = message
	if (request.method == 'GET'):
		if 'userid' in request.params:
			c.userid = request.params['userid']
	    	else:
			c.userid = userid
		for user in users:			
			if (user['userid'] == c.userid):
				c.image = user['image']

		return json.dumps({ 'userid': c.userid, 'image': c.image })
	
	elif (request.method == 'DELETE'):
		if 'userid' in request.params:
			c.userid = request.params['userid']
		else:
			c.userid = userid

		cursor = db.cursor()
		
		try:
			cursor.execute(""" DELETE FROM users WHERE userid = %s """, (userid))
			db.commit()
			c.message = "Successfully deleted %s" % c.userid
		except:
			c.message = "%s does not exist" % c.userid
			
		cursor.close()
		return c.message
	else:
		return request.method;

    def play(self, userid):
	global users
	global message
	c.users = users
	c.message = message
	if 'userid' in request.params:
		c.userid = request.params['userid']
    	else:
		c.userid = userid

	for user in users:
		if (user['userid'] == c.userid):
			c.image = user['image']
	return render('/play.mako')

    def message(self, msg):
	global message

	if (request.method == "POST"):
		if (msg != ''):
			message = msg
	elif (request.method == "DELETE"):
		message = ''
	else:
		# Not supported
		return
    
