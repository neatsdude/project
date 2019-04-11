#!/usr/bin/python3      -tt

import os
import requests
import mysql.connector

def main():

# Getting requested numbers
# Make sure the Base_new.txt is in same location as the script

    msisdn = os.popen(cut -d, -f1 Base_new.txt).readlines()
    for i in range(len(msisdn)):
        msisdn[i] = msisdn[i].rstrip('\n')

    clip_id = os.popen(cut -d, -f2 Base_new.txt).readlines()
    for i in range(len(clip_id)):
        clip_id[i] = clip_id[i].rstrip('\n')

# Database fetching

    db = mysql.connector.connect(host = '10.110.83.20', database = 'rbt', user = 'root', password = 'onmobile')
    query = '''SELECT * FROM rbt_subscriber;'''
    cursor = db.cursor()
    cursor.execute(query)
    data = cursor.fetchall()

# Making existing subscribers list in database

    subs_act_d = {}

    for i in range(data):
        subs_id = (data[i][0]).decode("utf-8")
        act_detail = (data[i][11]).decode("utf-8")
        subs_act_d[subs_id] = act_detail

# New directory report where activation logs file is there

    os.mkdir(report)

# Creating Log file ACTIVATION_REPORT.txt

    file = open('ACTIVATION_REPORT.txt' , 'w+')

# Getting the msisdn details one by one
# checking the subsribers activation details

    for num in range(msisdn):
        if subs_act_d[msisdn[num]] not in 'B' or 'Z' or 'G' or 'A' or 'N' or 'D' or 'P':

# URL parameters

            params = (
                        ('MSISDN', '%s'),
                        ('TONE_ID', '%s'),
                        ('REQUEST', 'SELECTION'),
                        ('SUB_TYPE', 'Prepaid'),
                        ('SELECTED_BY', 'CCC'),
                        ('CATEGORY_ID', '3'),
                        ('ISACTIVATE', 'TRUE'),
                        ('USE_UI_CHARGE_CLASS', 'TRUE'),
                        ('SUBSCRIPTION_CLASS', 'DEFAULT'),
                        ('CHARGE_CLASS', 'FREE_CHURN'),
                        ('IN_LOOP', 'TRUE'),
                    )%(msisdn[num] , clip_id[num])

# Getting URL resopnse

            response = requests.get('http://10.110.83.20:8080/rbt/rbt_promotion.jsp', params=params)

# Writing activation log

            file.write("%s,%s,"%(msisdn[num] , clip_id[num]) + response.text + ','+ response.url + '\n')

# If already activated write in activation log

        else:
            file.write("%s : ACTIVENUMBER\n" % (msisdn[num]))
        
    file.close()
        
# Boiler Plate

if __name__ == '__main__':
    main()
