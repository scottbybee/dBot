#!/usr/bin/python

###general
def imported():
  print "myDbTools is available!"

###DatabaseConnectivity
def connect():
  import sqlite3
  conn = sqlite3.connect('tools.db')
  return conn

def cursor(conn):
  c = conn.cursor()
  return c

###DatabaseDefaults
def rebuild_all(c):
  groups_table(c)
  groups_load(c)
  users_table(c)
  users_load(c)
  tools_table(c)
  tools_load(c)

def groups_table(c):
  c.execute('''DROP TABLE groups''')
  c.execute('''CREATE TABLE groups(id, name, description))''')

def groups_load(c):
  groups = [
	  (0,'PUBS','Poor Ugly Bikers!'),
	  (1,'Majestic','Majestic Lane Residents')
          ]
  c.executemany('INSERT INTO groups VALUES (?,?,?)', tools)
  
def tools_table(c):
  c.execute('''DROP TABLE tools''')
  c.execute('''CREATE TABLE tools (id, name, owner, deposit, fullPrice, fee, available)''')

def load_tools(c):
  tools = [
	  (0,'ladder',1,0,200,7,1),
	  (1,'torqueWrench 1/2inche drive',1,0,40,5,1),
	  (2,'torqueWrench 3/8inche drive',1,0,40,5,1),
	  (3,'diesel filter socket set',1,0,40,5,1)
          ]
  c.executemany('INSERT INTO tools VALUES (?,?,?,?,?,?)', tools)

def users_table(c):
  c.execute('''DROP TABLE users''')
  c.execute('''CREATE TABLE users (id, group, username, passsword, displayName)''')

def load_users(c):
  users = [
	(0,1,'test','test','test'),
        (1,0,'scott','test','Scott Bybee'),
        (2,0,'brian','test','Brian Bybee'),
        (3,0,'jim','test','Jim'),
        (4,0,'stan','test','Stan D'),
        (5,1,'scott','test','Scott Bybee')
        ]
  c.executemany('INSERT INTO users VALUES (?,?,?,?)', users)

def drink_ingredients_table(c):
  c.execute('''DROP TABLE drink_ingredients''')
  c.execute('''CREATE TABLE drink_ingredients (drinkID,ingredient,volume)''')

def load_drink_ingredients(c):
  #the 45 is ml - ~1.5oz
  drink_ingredients = [
    (0,1,45),(0,2,45),
    (1,0,45),(1,3,45),
    (2,1,45),(2,6,45),
    (3,4,45),(3,8,45)
    ]
  c.executemany('INSERT INTO drink_ingredients VALUES (?,?,?)', drink_ingredients)

###ApplicationQueries
def get_tools(c):
  #returns alpha sorted list of all tools and status
  tools = {}
  i=0
  for row in c.execute('SELECT id,name,available FROM tools ORDER BY name'):
    tools[i]=row[1],row[0],row[2]
    i=i+1
  return tool

def get_users(c):
  #returns just userID and displayName
  users = {}
  for row in c.execute('SELECT * FROM users'):
    users[row[0]]=row[3]
  return users

def get_drink_names(c):
  #return a list of drink in db order; not currently used
  drinkNames = {}
  for row in c.execute('SELECT * FROM drinks ORDER BY name ASC'):
    drinkNames[row[0]]=row[1]
  return drinkNames

def get_drink_names_index(c):
  #return a dictionary of display (alpha) order = drinkID
  drinksIndex = {}
  i=0
  for row in c.execute('SELECT * FROM drinks ORDER BY name ASC'):
    drinksIndex[i]=row[0]
    i=i+1
  return drinksIndex

def get_drink_names_alpha(c):
  #returns a list of drink names in alpha order
  drinkNamesAlpha = {}
  i=0
  for row in c.execute('SELECT * FROM drinks ORDER BY name ASC'):
    drinkNamesAlpha[i]=row[1]
    i=i+1
  return drinkNamesAlpha

def get_ingredients(c):
  #returns all ingredients; used to initialize robot 
  ingredients = {}
  for row in c.execute('SELECT * FROM ingredients' ):
    ingredients[row[0]]=row[2]
  return ingredients

def get_drink_ingredients(c, drinkID):
  #returns ingredients for a particular drink
  drinkIngredients = {}
  c.execute('SELECT * FROM drink_ingredients WHERE drinkID=?', (drinkID,))
  rows = c.fetchall()
  for row in rows:
    drinkIngredients[row[1]]=row[2]
  return drinkIngredients

