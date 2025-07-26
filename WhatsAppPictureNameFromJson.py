import os
import json
from exif import Image, DATETIME_STR_FORMAT
from datetime import datetime
import pytz

filesnames = os.listdir("Input/")
number = 0

for file in filesnames:
    if file.endswith('.jpg'):

        # input path
        FileName = file.replace(".jpg", "")
        InputPath = 'Input/' + FileName

        Opend = False
        with open(InputPath + '.jpg.json', 'r') as datei:
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

             # set timestamp
            image = Image(InputPath + '.jpg')
            image.make = "Python"
            image.datetime_digitized = DtScan.strftime(DATETIME_STR_FORMAT)
            with open(InputPath + '.jpg', 'wb') as new_image_file:
                new_image_file.write(image.get_file())

            # rename files
            OutputPath = 'Output_WA/WA_' + DtScan.strftime("%Y") + DtScan.strftime("%m") + DtScan.strftime("%d") + DtScan.strftime("%H") + DtScan.strftime("%M") + DtScan.strftime("%S") + '_' + str(number)
            os.rename(InputPath + '.jpg', OutputPath + '.jpg')

        if Opend:
            os.rename(InputPath + '.jpg.json', OutputPath + '.jpg.json')

print("Anzahl der Bilder: " + str(number))