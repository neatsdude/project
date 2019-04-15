#!/usr/local/bin/python3.7      -tt

import os
import requests
import mysql.connector

def main():
        db = mysql.connector.connect(host = '127.0.0.1', user = 'root', passwd = 'onmobile', database = 'test_rbt')
        query = '''SELECT * FROM rbt_subscriber;'''
        cursor = db.cursor()
        cursor.execute(query)
        data = cursor.fetchall()

# Making existing subscribers list in database

        subs_act_d = {}

        for i in range(len(data)):
                subs_id = (data[i][0]).decode("utf-8")
                act_detail = (data[i][11]).decode("utf-8")
                subs_act_d[subs_id] = act_detail

# New directory report where activation logs file is there

        os.mkdir('report')
        os.chdir('report')

# Creating Log file ACTIVATION_REPORT.txt

        file = open('Activation_status_REPORT.txt' , 'w+')



# URL parameters
        url = '''http://10.33.116.123:8080/rbt/rbt_promotion.jsp'''
        

# Check status for the msisdn in database

        for i in subs_act_d:
                params = (
            ('MSISDN' , i),
            ('REQUEST', 'STATUS')
                    )

# Getting URL resopnse
                response = requests.get(url, params=params)

# Writing logs
                file.write("%s : %s \n url:%s \n" % (i, response.text, response.url))

#               print("%s : %s :%s" % (i, response.text,response.url))

        file.close()
        print('Logs are being written to Activation_status_REPORT.txt file')

# Boiler Plate

if __name__ == '__main__':
        main()
