import os
from exif import Image, DATETIME_STR_FORMAT
from datetime import datetime

filesnames = os.listdir("Input/")
number = 0
NumberNonLive = 0
NumberSkiped = 0

for file in filesnames:
    if file.endswith('.JPG'):

        # input path
        FileName = file.replace('.JPG', '')
        InputPath = 'Input/' + FileName

        try:
            # get timestamp
            image = Image(InputPath + '.JPG')

            #ReadTimestamp = image.datetime_original
            #ReadDateAndTime = ReadTimestamp.split(" ")
            #ReadDate = ReadDateAndTime[0].split(":")
            #ReadTime = ReadDateAndTime[1].split(":")
            #Timestamp = ReadDate[0] + ReadDate[1] + ReadDate[2] + ReadTime[0] + ReadTime[1] + ReadTime[2]
            DtScan = datetime(year=2012, month=7, day=15, hour=0, minute=0, second=0)
            #image.datetime_original = DtScan.strftime(DATETIME_STR_FORMAT)

            #ReadTimestamp = image.datetime
            #ReadDateAndTime = ReadTimestamp.split(" ")
            #ReadDate = ReadDateAndTime[0].split(":")
            #ReadTime = ReadDateAndTime[1].split(":")
            #Timestamp = ReadDate[0] + ReadDate[1] + ReadDate[2] + ReadTime[0] + ReadTime[1] + ReadTime[2]
            #DtScan = datetime(year=int(ReadDate[0]), month=int(ReadDate[1]), day=int(ReadDate[2]), hour=int(ReadTime[0]), minute=int(ReadTime[1]), second=int(ReadTime[2]))
            image.datetime_digitized = DtScan.strftime(DATETIME_STR_FORMAT)
            #image.make = "Python"
            
            with open(InputPath + '.JPG', 'wb') as new_image_file:
                new_image_file.write(image.get_file())

            # id
            number += 1

            # rename files
            OutputPath = 'Output_IMG/IMG_' + DtScan.strftime("%Y") + DtScan.strftime("%m") + DtScan.strftime("%d") + DtScan.strftime("%H") + DtScan.strftime("%M") + DtScan.strftime("%S") + '_' + str(number)
            os.rename(InputPath + '.JPG', OutputPath + '.JPG')
            try:
                os.rename(InputPath + '.MOV', OutputPath + '.MOV')
            except:
                NumberNonLive += 1
        except:
            NumberSkiped += 1

print("Anzahl der Bilder: " + str(number))
print("Anzahl nicht Live Bilder: " + str(NumberNonLive))
print("Anzahl Bilder übersprungen: " + str(NumberSkiped))