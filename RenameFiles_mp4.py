import os
import json
from exif import Image, DATETIME_STR_FORMAT
from datetime import datetime
import pytz

## mp4 Dateien
FileEnding = "mp4"
OUTPUT_PATH = "Output_WA/"
if not os.path.exists(OUTPUT_PATH):
    os.mkdir(OUTPUT_PATH)

INPUT_PATH = "Input_S_mp4/"
filesnames = os.listdir(INPUT_PATH)

FileCnt = 0
for file in filesnames:
    if file.endswith('.json'):

        if ("." + FileEnding) not in file:
            continue
        else:
            File_json = file
            FoundFile = file.split(("." + FileEnding))
            FoundFile = FoundFile[0] + ("." + FileEnding)

            with open(INPUT_PATH + file, 'r') as datei:
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
                OutputPath = OUTPUT_PATH + "WA_" + DtScan.strftime("%Y") + DtScan.strftime("%m") + DtScan.strftime("%d") + DtScan.strftime("%H") + DtScan.strftime("%M") + DtScan.strftime("%S") + "_" + str(FileCnt+1)
                if os.path.exists(INPUT_PATH + FoundFile):
                    os.rename(INPUT_PATH + FoundFile, OutputPath + "." + FileEnding)
                    print(FoundFile)
                    FileCnt += 1

print("Anzahl der Bilder: " + str(FileCnt))
