import logging
import json
import MySQLdb
from networkingserver.model.database import databaseModel
from networkingserver.model.userModel import userModel
import collections
import signal

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from networkingserver.lib.base import BaseController, render

log = logging.getLogger(__name__)


users = [{'userid': 'fox', 'image': '/img/fox.gif'}, {'userid': 'peppy', 'image': '/img/peppy.gif'}]
message = ""

database = databaseModel()
database.connect()
db = database.getConnection()
if db == None:
		print "Failed to connect to the database"

user = userModel()

c.authenticated = False

class MaincontrollerController(BaseController):
    def auth(self):
    	userid = user.auth(request)
    	return userid

    def index(self):
			global users;
			global message
			global user;
			c.users = users;
			c.message = message

			if (request.method == 'GET'):
				c.username = user.auth(request)
				if (c.username):
						c.authenticated = True
						return render('/dashboard.mako')
				else:
						c.authenticated = False
						return render('/index.mako')
			else:
				return request.method;

    def login(self):
			global db
			global user
			if 'username' in request.params and 'password' in request.params:
				uname = request.params['username']
				passwd = request.params['password']

				if (user.login(uname, passwd, db)):
						response.set_cookie( "authenticated" , uname, max_age=180*24*3600 )
						return "Valid"
				else:
						return "Invalid"


    def logout(self):
			response.delete_cookie('authenticated')
			return

    def dashboard(self, username):
			global users
			global message
			c.users = users
			c.message = message
			c.username = username

			c.authenticated = user.auth(request)
			if (c.authenticated):
				return render('/dashboard.mako')
			else:
				c.authenticated = False
				return render('/index.mako')

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
					cursor.execute("""SELECT userid, username, password FROM dan_Users""")
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
				try:
					cursor.execute("""INSERT into dan_Users (username, password) VALUES(%s, %s)""", (uname, passwd))
					db.commit()
					c.message = ("Successfully added ", (uname))
				except:
					c.message = "Failed to add user %s, that user already exists" % (uname)

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
					cursor.execute(""" DELETE FROM dan_Users WHERE userid = %s """, (userid))
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
