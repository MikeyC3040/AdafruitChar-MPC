from __future__ import unicode_literals

from threading import Timer
from mpd import MPDClient
import Adafruit_CharLCD as LCD
from lcd import Background
from time import sleep
import datetime, signal
from datetime import timedelta, datetime
lcd = LCD.Adafruit_CharLCDPlate()
back = Background(lcd)		
	
def main():
	signal.signal(signal.SIGTERM, back.quit_nicely)
	buttons = ( (LCD.SELECT, 'Select'),
				(LCD.LEFT,   'Left'  ),
				(LCD.UP,     'Up'    ),
				(LCD.DOWN,   'Down'  ),
				(LCD.RIGHT,  'Right' ) )
	updateTime = datetime.now()
	try:		
		while True:
			for b in buttons:
				if lcd.is_pressed(b[0]):
					back.button(b[1])
					sleep(.2)
			if updateTime < datetime.now():
				updateTime = datetime.now()+timedelta(milliseconds=500)
				back.refresh_mpd()
				back.display()
	except KeyboardInterrupt:
		back.quit_nicely()

main()
