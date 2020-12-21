import pandas as pd
from dateutil.parser import parse
from playsound import playsound

carprobe = pd.read_csv('carprobe.csv')

def getSpeed(s):
  return s>50

def getTimeDelta(dt1, dt2):
  datetime1 = parse(dt1)
  datetime2 = parse(dt2)
  delta=(datetime2-datetime1).total_seconds()
  return delta>=3

def getDrift(d1, d2):
  return abs(d2-d1)>15

for i in range(1, carprobe.index.stop):
  time = getTimeDelta(carprobe['local_time'][i-1], carprobe['local_time'][i])
  speed = getSpeed(carprobe['speed'][i])
  drift = getDrift(carprobe['heading'][i-1], carprobe['heading'][i])
  if speed and time and drift:
    print(i)
    playsound('censor-beep-3.mp3')
