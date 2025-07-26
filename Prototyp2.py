import os
from exif import Image, DATETIME_STR_FORMAT
from datetime import datetime

filesnames = os.listdir("Input/")
number = 0
NumberNonLive = 0
NumberSkiped = 0

for file in filesnames:
    if file.endswith('.jpg'):

        # input path
        FileName = file.replace('.jpg', '')
        InputPath = 'Input/' + FileName

        try:
            # get timestamp
            image = Image(InputPath + '.jpg')

            ReadDate = FileName.split("-")
            ReadYear = ReadDate[1][0] + ReadDate[1][1] + ReadDate[1][2] + ReadDate[1][3]
            ReadMonth = ReadDate[1][4] + ReadDate[1][5]
            ReadDay = ReadDate[1][6] + ReadDate[1][7]
            DtScan = datetime(year=int(ReadYear), month=int(ReadMonth), day=int(ReadDay), hour=0, minute=0, second=0)

            image.make = "Python"
            image.datetime_digitized = DtScan.strftime(DATETIME_STR_FORMAT)
            with open(InputPath + '.jpg', 'wb') as new_image_file:
                new_image_file.write(image.get_file())

            # id
            number += 1

            # rename files
            OutputPath = 'Output_WA/WA_' + DtScan.strftime("%Y") + DtScan.strftime("%m") + DtScan.strftime("%d") + DtScan.strftime("%H") + DtScan.strftime("%M") + DtScan.strftime("%S") + '_' + str(number)
            os.rename(InputPath + '.jpg', OutputPath + '.jpg')
            try:
                os.rename(InputPath + '.MOV', OutputPath + '.MOV')
            except:
                NumberNonLive += 1
        except:
            NumberSkiped += 1

print("Anzahl der Bilder: " + str(number))
print("Anzahl nicht Live Bilder: " + str(NumberNonLive))
print("Anzahl Bilder übersprungen: " + str(NumberSkiped))