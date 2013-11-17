import MySQLdb

class userModel():
  def auth(self, request):
    return request.cookies.get( "authenticated" )

  def login(self, username, password, db):
      # Check if username and password tuple exist in DB
      cursor = db.cursor()
      cursor.execute("""
          SELECT username, password
            FROM dan_Users
            WHERE username = %s
            AND BINARY password = %s""", (username, password))
      result = cursor.fetchone()
      if result == None:
        return False
      else:
        return True

  def logout(self):
    self.db.close()