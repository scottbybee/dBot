#!/usr/bin/python

# contains the funtions I need to interact with the database

def imported():
  print "database.py is available!"

def get_drinks():
  c.execute('Select * from drinks ORDER BY name ASC;')

def display_drinks():
  c.execute()

