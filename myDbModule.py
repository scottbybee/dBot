#!/usr/bin/python

###general
def imported():
  print "myDbModule is available!"

###DatabaseConnectivity
def connect():
  import sqlite3
  conn = sqlite3.connect('drinks.db')
  return conn

def cursor(conn):
  c = conn.cursor()
  return c

###DatabaseDefaults
def drinks_table(c):
  c.execute('''DROP TABLE drinks''')
  c.execute('''CREATE TABLE drinks (id, name)''')

def load_drinks(c):
  drinks = [
            (0,'Crown-7'),(1,'Jack & Coke'),
            (2,'Brandy-7'),(3,'Diet & Malibu'),
            (4,'TEST DRINK ONE')
           ]
  c.executemany('INSERT INTO drinks VALUES (?,?)', drinks)

def ingredients_table(c):
  c.execute('''DROP TABLE ingredients''')
  c.execute('''CREATE TABLE ingredients (id, name, displayName)''')

def load_ingredients(c):
  ingredients = [
            (0,'cola',"Coke"),
            (1,'limeSoda',"7-Up"),
            (2,'whiskey',"Crown Royal/Black Velvet"),
            (3,'bourbon',"Jack/Evan"),
            (4,'dietCola',"Diet Coke"),
            (5,'tonic',"Tonic"),
            (6,'brandy',"Brandy"),
            (7,'vodka',"Svedka"),
            (8,'coconutRum',"Malibu Rum"),
            (9,'spicedRum',"Capt'n"),
            (10,'jagemeister',"Jag"),
            (11,'tequila',"ta-Kill-Ya!")
            ]
  c.executemany('INSERT INTO ingredients VALUES (?,?,?)', ingredients)

def load_ingredients2(c):
  ingredients = [
            (0,'whiskey',"Crown Royal/Black Velvet"),
            (1,'bourbon',"Jack/Evan"),
            (2,'brandy',"Brandy"),
            (3,'vodka',"Svedka"),
            (4,'coconutRum',"Malibu Rum"),
            (5,'spicedRum',"Capt'n"),
            (6,'jagemeister',"Jag"),
            (7,'tequila',"ta-Kill-Ya!"),
            (8,'gren',"Grenidean - spelled incorrectly on purpose"),
            (9,'cran',"cranberry Juice"),
	    (10,'pineapple',"pineapple Juice"),
            (11,'orange',"OJ"),
            (12,'7',"7-up"),
            (13,'cola',"cola"),
            (14,'dietCola',"Diet Cola"),
            (15,'tonic',"tonic")            
]
  c.executemany('INSERT INTO ingredients VALUES (?,?,?)', ingredients)


def drink_ingredients_table(c):
  c.execute('''DROP TABLE drink_ingredients''')
  c.execute('''CREATE TABLE drink_ingredients (drinkID,ingredient,volume)''')

def load_drink_ingredients(c):
  #the 45 is ml - ~1.5oz
  drink_ingredients = [
    (0,1,45),(0,2,45),
    (1,0,45),(1,3,45),
    (2,1,45),(2,6,45),
    (3,4,45),(3,8,45),
    (4,0,30),(4,1,30),(4,2,30),(4,3,30),(4,4,30),(4,5,30),(4,6,30),(4,7,30)
    ]
  c.executemany('INSERT INTO drink_ingredients VALUES (?,?,?)', drink_ingredients)

###ApplicationQueries
def get_drinks(c):
  #not currently used, but leaving in case I go back to single query design.
  drinks = {}
  i=0
  for row in c.execute('SELECT * FROM drinks ORDER BY name'):
    #drinks[row[0],"info"]=row[2],row[3],row[4],row[5]
    #drinks[row[0],"name"]=row[1]
    drinks["name",row[0]]=row[1]
    i=i+1
  drinks['count']=i
  #get_ingredients(c, drinks)
  #get_drink_ingredients(c, drinks)
  return drinks

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

