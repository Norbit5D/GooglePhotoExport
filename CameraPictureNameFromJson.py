import os
import json
from exif import Image, DATETIME_STR_FORMAT
from datetime import datetime
import pytz

filesnames = os.listdir("Input/")
number = 0
NumberNonLive = 0

for file in filesnames:
    if file.endswith('.JPG'):

        # input path
        FileName = file.replace(".JPG", "")
        InputPath = 'Input/' + FileName

        Opend = False
        with open(InputPath + '.JPG.json', 'r') as datei:
            Opend = True

            # id
            number += 1

            # get timestamp
            dictionary = json.load(datei)
            photoTakenTime = dictionary["photoTakenTime"]
            timestamp = photoTakenTime['timestamp']

            LocalTime = datetime.fromtimestamp(int(timestamp), pytz.UTC)
            TimeZone = pytz.timezone('Europe/Berlin')
            iYear   = int(format(TimeZone.normalize(LocalTime.astimezone(TimeZone)), '%Y'))
            iMonth  = int(format(TimeZone.normalize(LocalTime.astimezone(TimeZone)), '%m'))
            iDay    = int(format(TimeZone.normalize(LocalTime.astimezone(TimeZone)), '%d'))
            iHour   = int(format(TimeZone.normalize(LocalTime.astimezone(TimeZone)), '%H'))
            iMinute = int(format(TimeZone.normalize(LocalTime.astimezone(TimeZone)), '%M'))
            iSecond = int(format(TimeZone.normalize(LocalTime.astimezone(TimeZone)), '%S'))
            DtScan = datetime(year=iYear, month=iMonth, day=iDay, hour=iHour, minute=iMinute, second=iSecond)

            # rename files
            OutputPath = 'Output_IMG/IMG_' + DtScan.strftime("%Y") + DtScan.strftime("%m") + DtScan.strftime("%d") + DtScan.strftime("%H") + DtScan.strftime("%M") + DtScan.strftime("%S") + '_' + str(number)
            os.rename(InputPath + '.JPG', OutputPath + '.JPG')
            try:
                os.rename(InputPath + '.MP4', OutputPath + '.MP4')
            except:
                NumberNonLive += 1

        if Opend:
            os.rename(InputPath + '.JPG.json', OutputPath + '.JPG.json')

print("Anzahl der Bilder: " + str(number))
print("Anzahl nicht Live Bilder: " + str(NumberNonLive))