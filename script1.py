#!/usr/bin/python
import os #seems a waste to import this just to clear the screen
# see if you can use some code to clear it.

import RPi.GPIO as GPIO
import time

import myDbModule as db

db.imported()
#connected();

conn = db.connect()
c = db.cursor(conn)
#db.drinks_table(c)
#db.default_drinks(c)
#conn.commit() #save the data in the table

os.system('clear')

drinks = db.display_drinks(c)

GPIO.setmode(GPIO.BCM)
# what other modes are there??

# init list with pin numbers
pinList = [2, 3, 4, 17]
# using a 4 channel releay module
#will add a 8 channel ssr module soon
#pinList = [2,3,4,17,27,22,10,9,11,5,6,13]
#channel[
# loop through pins and set mode and state to 'high'
for i in pinList: 
    GPIO.setup(i, GPIO.OUT) 
    GPIO.output(i, GPIO.HIGH)

# time to pour each ingredient
#pourTime = [0.5, 1, 2, 3] # create an array with run time per channel
#global drinks
print ''
print "Insert an appropriately sized glass with ice in the dispenser!"
drinkID = input("Then, and only then, select your drink: ")
print drinkID
pourTime = drinks[drinkID]
# names for display
poisonList = ["Cola", "Bourbon", "Rum", "Whiskey"]


# main loop  - convert to a loop for ch 

try:
  print "Pouring your drink..."
  print ''
  ch=0
  if pourTime[ch]:
    GPIO.output(pinList[ch], GPIO.LOW)
    print poisonList[ch]
    time.sleep(pourTime[ch]);
    GPIO.output(pinList[ch], GPIO.HIGH) 
  
  ch = 1
  if pourTime[ch]:
    GPIO.output(pinList[ch], GPIO.LOW)
    print poisonList[ch]
    time.sleep(pourTime[ch]);  
    GPIO.output(pinList[ch], GPIO.HIGH) 
  
  ch = 2
  if pourTime[ch]:
    GPIO.output(pinList[ch], GPIO.LOW)
    print poisonList[ch]
    time.sleep(pourTime[ch]);
    GPIO.output(pinList[ch], GPIO.HIGH) 

  ch=3
  if pourTime[ch]:
    GPIO.output(pinList[ch], GPIO.LOW)
    print poisonList[ch]
    time.sleep(pourTime[ch]);
    GPIO.output(pinList[ch], GPIO.HIGH) 


  GPIO.cleanup()
  conn.close()
  print ''
  print "Enjoy Responsibly!"

# End program cleanly with keyboard
except KeyboardInterrupt:
  print "  Quit"

  # Reset GPIO settings
  GPIO.cleanup()


# find more information on this script at
# http://youtu.be/WpM1aq4B8-A

#So, here are docs for the dBot
#dBot is a machine to pour your favorite cocktail
#drinks are stored in the database
#4 ingredients are dispensed by this version:
# 0 - cola
# 1 - seven
# 2 - whiskey
# 3 - bourbon
#easy to expand to 12 ingredients by adding another relay module and pumps
# 4 - dietCola
# 5 - tonic
# 6 - brandy
# 7 - vodka
# 8 - malibu
# 9 - spiced
# 10 - kinky pink
# 11 - Jagermeister
# 12 - TaKillYa!!
# need a pump_prime() and pumps_wash script
# (might need a valve just below the pump to allow liquor to return to bottles)

### progress notes
# I added a db module to handle connecting to sqllite and storing drinks in the table
# right now, I have to add drinks by editing the script and running it again to drop and rebuild the table
# when the drinks are displayed, I create a dictionary and but the values for each drink in there
# I need to read a value and pour that drink. **DONE!!**

###

### Next Steps
# 0) clean up this code.  use queries to build dictionaries and use good, clear, logical structures
#    drinkNames, drinks, (leave pinList hardcoded)
#    seperate db and display.  build drinks dictionary in db module, but display locally
# 1) order ssr, motor, tubing, fittings & 12v suppply
# 2) wire up the motor
# 3) design and print a peristaltic pump for the dc motor
# 4) design some sort of rack to mount the hardware and hold the ingredients
# 5) start calibration 
###   
