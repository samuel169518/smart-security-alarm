from datetime import datetime
import tzevaadom
import os
from gtts import gTTS
import time

def handler(List_Alerts):
  for alert in List_Alerts:

    message = "Terorists : " + alert["name"] + ".area:  " + alert["zone"] 
    reversed = message[::-1] 
    print(reversed+ ", time: " + str(datetime.now()))
    if "enter your city 1" in reversed or "enter your city 2" in message:
        os.system("start alarm_real.mp3")

tzevaadom.alerts_listener(handler)