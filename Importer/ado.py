import sqlite3 as sql

from flask import g

class ADO():
	
	_database = None;
	
	DATABASE = r'model/data/partners.db'
	SCHEMA = r'model/schema/partners.sql'

	def __init__(self, app):
		try:
			self.__init_db__(app)

		except sql.Error, e:
			print "Error: %s" % e.args[0]
			raise
			
		finally:
			return	
	
	def __init_db__(self, app):
		try:
			db = self.__get_db__()
			
			with app.app_context():
				with app.open_resource(self.SCHEMA, mode='r') as f:
					db.cursor().executescript(f.read())
				db.commit()

		except sql.Error, e:
			print "Error: %s" % e.args[0]
			raise
		
		finally:
			return	
		
	def __get_db__(self):
		try:
			db = ADO._database
			if db is None:
				db = ADO._database = sql.connect(self.DATABASE)
			return db

		except sql.Error, e:
			print "Error: %s" % e.args[0]
			raise
			
		finally:
			return	

	##########################################################################
			
	def close_connection(self, exception):
		try:
			db = ADO._database;
			if db is not None:
				db.close()

		except sql.Error, e:
			print "Error: %s" % e.args[0]
			raise
		
		finally:
			return	

	##########################################################################

	def __query_db__(self, query, args=(), one=False):
		try:
			cur = self.get_db().execute(query, args)
			rv = cur.fetchall()
			cur.close()
			return (rv[0] if rv else None) if one else rv	

		except sql.Error, e:
			print "Error: %s" % e.args[0]
			raise
			
		finally:
			return	
			
	def getAll(self):
		try:		
			for partner in self.__query_db__('select * from partners'):
				print partner['name'], 'has the id', partner['id']

		except sql.Error, e:
			print "Error: %s" % e.args[0]
			raise
			
		finally:
			return	

	def queryByName(self, name):
		try:
			partner = self.__query_db__('select * from partners where name = ?',
			                [name], one=True)
			
			if partner is None:
				print 'No such partner'
				
			else:
				print name, 'has the id', partner['id']
				
						
		except sql.Error, e:
			print "Error: %s" % e.args[0]
			raise
			
		finally:
			return	

	##########################################################################
	
	def __exec_db__(self, query, args=()):
		try:
			cur = self.get_db().execute(query, args)
			cur.close()

		except sql.Error, e:
			print "Error: %s" % e.args[0]
			raise
			
		finally:
			return	
	
	def createPartner(self, name, slug, spx_path, img_path):
		try:
			self.__exec_db__(
				"""INSERT INTO 
					partners (name, slug, spread_sheet_path, img_path) 
					VALUES ('?','?','?', '?')""",
			                [name, slug, spx_path, img_path])
								
		except sql.Error, e:
			print "Error: %s" % e.args[0]
			raise
			
		finally:
			return	
			
	def updatePartner(self, name, slug, spx_path, img_path):
		self.__exec_db__(
			"""UPDATE partners 
				SET slug='?', spread_sheet_path='?', img_path='?'   
				WHERE name='?'""",
		                [name, slug, spx_path, img_path])
		
		return        
			
	def deletePartner(self, name):
		try:
			self.__exec_db__(
				"DELETE FROM partners WHERE name = '?'", [name])
		
		except sql.Error, e:
			print "Error: %s" % e.args[0]
			raise
			
		finally:
			return	
			