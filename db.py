#!/usr/bin/python

# IMPORTANT NOTE
# Seems the 4 channel mechanical releay and the 8 channel SSR modules
# are different.  Opposite in fact.  One needs GPIO.LOW to turn on, the other is opposite.

###Imports - builtins
import os #seems a waste to import this just to clear the screen - see if you can use some code to clear it.
import RPi.GPIO as GPIO
import time




def primeChannel(pinID, timeout):
  GPIO.setmode(GPIO.BCM)
  #init pilist[ch-1]
  GPIO.setup(pinID, GPIO.OUT)
  GPIO.output(pinID, GPIO.HIGH)
  #take it low (ie. turn on pump)
  time.sleep(float(1.0))
  GPIO.output(pinID, GPIO.LOW)
  #sleep (let it run XX seconds)
  time.sleep(float(timeout));
  #take it high (shut off pump)
  GPIO.output(pinID, GPIO.HIGH)
  #cleanup (reset for next use)
  GPIO.cleanup()

###display the available drinks on screen
os.system('clear')


primeChannel(4,5)


###Allow user to select her drink
print ''
drinkIndexID = input("Then, and only then, select your drink: ")
#print 'drink_ingredients: ',drink_ingredients
###initialize the hardware
GPIO.setmode(GPIO.BCM) ##continue to use BCM because I believe only BCM is supported when using PWM
#init list with pin numbers
#pinList = [2, 3, 4, 17] # using a 4 channel releay module
#pinList = [4,17,27,22,18,23,24,25] # using 8 channel module
#pinList = [2,3,4,17,27,22,10,9,11,5,6,13] # using both modules 
#pinList = [4,17,27,22,5,6,13,19,23,24,25,12,16,20,21,26] # using 16 channel module (green ones) 
pinList = [4,17,27,22,5,6,13,19,18,23,24,25,12,16,20,26] # using 16 channel module (green ones) 
# loop through pins and set mode to 'out' and state to 'high'
for i in pinList:
	GPIO.setup(i, GPIO.OUT)
	GPIO.output(i, GPIO.HIGH)

###Pour the drinkt
try:
  print "Pouring your drink..."
  for i in range(len(ingredients)):
    if drink_ingredients.get(i):
      GPIO.output(pinList[i], GPIO.LOW)
      print "Pouring:",channelList[i]
      time.sleep(float(drink_ingredients[i]/15))
      GPIO.output(pinList[i], GPIO.HIGH)
  GPIO.cleanup()
  conn.close()
  print ''
  print "Enjoy Responsibly!"


# End program cleanly with keyboard
except KeyboardInterrupt:
  print "  Quit"
  # Reset GPIO settings
  GPIO.cleanup()


###so, there you have it.  A good basic but functional drinkBot!!
#docs for the dBot
#dBot is a machine to pour your favorite cocktail
#drinks are stored in the database
#12-16 ingredients are dispensed by this version:
# 0 - cola
# 1 - seven
# 2 - whiskey
# 3 - bourbon
# 4 - dietCola
# 5 - tonic
# 6 - brandy
# 7 - vodka
# 8 - malibu
# 9 - spiced
# 10 - Jagermeister
# 11 - TaKillYa!!
# need a pump_prime() script
# (might need a valve just below the pump to allow liquor to return to bottles)
#
# I added a db module to handle connecting to sqllite and storing drink infos in the table
# I have to add drinks by editing the script and running it again to drop and rebuild the table
# I use a dictionary to display all drinks
# I need to read a value, query the database, and finally pour that drink
#
# Next Steps
# 0) clean up this code. DONE
# add code to list drinks by alpha
# 1) order ssr, motor, tubing, fittings & 12v suppply
# 2) wire up the motor
# 3) design and print a peristaltic pump for the dc motor
# 4) design some sort of rack to mount the hardware and hold the ingredients
# 5) start calibration testing.  ;-)
###   

