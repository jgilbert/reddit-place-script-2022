#!/usr/bin/env python3

import csv
import sys

alts = list()

with open(sys.argv[1], newline='') as csvfile:
    myreader = csv.DictReader(csvfile)
    for row in myreader:
        alts.append(row)

width = int(sys.argv[2])
height = int(sys.argv[3])
numenvs = int(len(alts)/2)
width_start = int(width/2)
height_interval = int(height/numenvs)

count = 0
for x in range(numenvs):
    usernames = [ x["account_username"] for x in alts[count:count+2] ]
    passwords = [ x["account_password"] for x in alts[count:count+2] ]
    clientid = [ x["client_key"] for x in alts[count:count+2] ]
    secretid = [ x["secret_key"] for x in alts[count:count+2] ]
    with open(f"env{int(count/2)}.out", "w") as out:
        line = "ENV_PLACE_USERNAME='[" + ",".join([f'"{x}"' for x in usernames]) + "]'\n"
        out.write(line)
        line = "ENV_PLACE_PASSWORD='[" + ",".join([f'"{x}"' for x in passwords]) + "]'\n"
        out.write(line)
        line = "ENV_PLACE_APP_CLIENT_ID='[" + ",".join([f'"{x}"' for x in clientid]) + "]'\n"
        out.write(line)
        line = "ENV_PLACE_SECRET_KEY='[" + ",".join([f'"{x}"' for x in secretid]) + "]'\n"
        out.write(line)
        out.write('ENV_DRAW_X_START="300"\n')
        out.write('ENV_DRAW_Y_START="450"\n')
        out.write(f"ENV_R_START='[\"{count*height_interval}\", \"{count*height_interval}\"]'\n")
        out.write(f"ENV_C_START='[\"{0}\", \"{width_start}\"]'\n")
    count += 2
