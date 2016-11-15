# my_alarm_clock.py
# David Snider
# 10/18/2016
import time
import winsound
import tunes

beep = winsound.Beep

answer = ''
while answer != 'y':
    alarmTime = input("Give time for alarm(HH:MM)(24hr time) ")
    answer = input("Is "+alarmTime+" the correct time?(y/n) ")

alarmTime = alarmTime.split(":")
hour = int(alarmTime[0])
minute = int(alarmTime[1])
isAlarm = False
while not isAlarm:
    now = time.localtime()
    if now.tm_hour == hour and now.tm_min == minute:
        isAlarm = True
    else:
        time.sleep(5)

while True:
    for i in range(1,40):
        beep(i*100,200)
    for i in range(40,0,-1):
        beep(i*100,200)

    tunes.alarm_tone()
    for i in range(8):
        beep(1000,1000)
    
