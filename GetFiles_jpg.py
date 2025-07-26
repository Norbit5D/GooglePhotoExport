import os
import json
from exif import Image, DATETIME_STR_FORMAT
from datetime import datetime
import pytz

## JPG Dateien + Live MP4
FileEnding = "JPG"
OUTPUT_PATH = "Input_B_" + FileEnding + "/"
if not os.path.exists(OUTPUT_PATH):
    os.mkdir(OUTPUT_PATH)

INPUT_PATH = "Input/"
filesnames = os.listdir(INPUT_PATH)

FileCnt = 0
LiveCnt = 0
for file in filesnames:
    if file.endswith('.json'):

        if ("." + FileEnding) not in file:
            continue
        else:
            File_json = file
            FoundFile = file.split(("." + FileEnding))
            LiveFile = FoundFile[0] + (".MP4")
            FoundFile = FoundFile[0] + ("." + FileEnding)
            if os.path.exists(INPUT_PATH + FoundFile):
                os.rename(INPUT_PATH + File_json, OUTPUT_PATH + File_json)
                os.rename(INPUT_PATH + FoundFile, OUTPUT_PATH + FoundFile)
                FileCnt += 1
                print(FoundFile)
            if os.path.exists(INPUT_PATH + LiveFile):
                os.rename(INPUT_PATH + LiveFile, OUTPUT_PATH + LiveFile)
                LiveCnt += 1
print("Es wurden " + str(FileCnt) + " Dateien von " + INPUT_PATH + " nach " + OUTPUT_PATH + " kopiert!")
print("Davon waren " + str(LiveCnt) + " Live Bilder")
print()

## MP4 Dateien
FileEnding = "MP4"
OUTPUT_PATH = "Input_B_" + FileEnding + "/"
if not os.path.exists(OUTPUT_PATH):
    os.mkdir(OUTPUT_PATH)

INPUT_PATH = "Input/"
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
            if os.path.exists(INPUT_PATH + FoundFile):
                os.rename(INPUT_PATH + File_json, OUTPUT_PATH + File_json)
                os.rename(INPUT_PATH + FoundFile, OUTPUT_PATH + FoundFile)
                FileCnt += 1
                print(FoundFile)
print("Es wurden " + str(FileCnt) + " Dateien von " + INPUT_PATH + " nach " + OUTPUT_PATH + " kopiert!")
print()

## jpg Dateien
FileEnding = "jpg"
OUTPUT_PATH = "Input_S_" + FileEnding + "/"
if not os.path.exists(OUTPUT_PATH):
    os.mkdir(OUTPUT_PATH)

INPUT_PATH = "Input/"
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
            if os.path.exists(INPUT_PATH + FoundFile):
                os.rename(INPUT_PATH + File_json, OUTPUT_PATH + File_json)
                os.rename(INPUT_PATH + FoundFile, OUTPUT_PATH + FoundFile)
                FileCnt += 1
                print(FoundFile)
print("Es wurden " + str(FileCnt) + " Dateien von " + INPUT_PATH + " nach " + OUTPUT_PATH + " kopiert!")
print()


## mp4 Dateien
FileEnding = "mp4"
OUTPUT_PATH = "Input_S_" + FileEnding + "/"
if not os.path.exists(OUTPUT_PATH):
    os.mkdir(OUTPUT_PATH)

INPUT_PATH = "Input/"
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
            if os.path.exists(INPUT_PATH + FoundFile):
                os.rename(INPUT_PATH + File_json, OUTPUT_PATH + File_json)
                os.rename(INPUT_PATH + FoundFile, OUTPUT_PATH + FoundFile)
                FileCnt += 1
                print(FoundFile)
print("Es wurden " + str(FileCnt) + " Dateien von " + INPUT_PATH + " nach " + OUTPUT_PATH + " kopiert!")
print()

## MOV Dateien
FileEnding = "MOV"
OUTPUT_PATH = "Input_B_" + FileEnding + "/"
if not os.path.exists(OUTPUT_PATH):
    os.mkdir(OUTPUT_PATH)

INPUT_PATH = "Input/"
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
            if os.path.exists(INPUT_PATH + FoundFile):
                os.rename(INPUT_PATH + File_json, OUTPUT_PATH + File_json)
                os.rename(INPUT_PATH + FoundFile, OUTPUT_PATH + FoundFile)
                FileCnt += 1
                print(FoundFile)
print("Es wurden " + str(FileCnt) + " Dateien von " + INPUT_PATH + " nach " + OUTPUT_PATH + " kopiert!")
print()

## PNG Dateien
FileEnding = "PNG"
OUTPUT_PATH = "Input_B_" + FileEnding + "/"
if not os.path.exists(OUTPUT_PATH):
    os.mkdir(OUTPUT_PATH)

INPUT_PATH = "Input/"
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
            if os.path.exists(INPUT_PATH + FoundFile):
                os.rename(INPUT_PATH + File_json, OUTPUT_PATH + File_json)
                os.rename(INPUT_PATH + FoundFile, OUTPUT_PATH + FoundFile)
                FileCnt += 1
                print(FoundFile)
print("Es wurden " + str(FileCnt) + " Dateien von " + INPUT_PATH + " nach " + OUTPUT_PATH + " kopiert!")
print()

## WEBP Dateien
FileEnding = "WEBP"
OUTPUT_PATH = "Input_B_" + FileEnding + "/"
if not os.path.exists(OUTPUT_PATH):
    os.mkdir(OUTPUT_PATH)

INPUT_PATH = "Input/"
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
            if os.path.exists(INPUT_PATH + FoundFile):
                os.rename(INPUT_PATH + File_json, OUTPUT_PATH + File_json)
                os.rename(INPUT_PATH + FoundFile, OUTPUT_PATH + FoundFile)
                FileCnt += 1
                print(FoundFile)
print("Es wurden " + str(FileCnt) + " Dateien von " + INPUT_PATH + " nach " + OUTPUT_PATH + " kopiert!")
print()