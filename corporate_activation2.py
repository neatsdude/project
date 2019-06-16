#!/usr/bin/python3  -tt

import os
import sys
import requests
import mysql.connector

# Global variable   url = 'http://172.27.102.56:8080/rbt/rbt_promotion.jsp?MSISDN=701890509&REQUEST=STATUS'

url = '''http://172.27.102.56:8080/rbt/rbt_promotion.jsp'''

def status_check(msisdn):
    if isinstance(msisdn, dict):
        for i in msisdn:
            params = (('MSISDN' , i), ('REQUEST', 'STATUS'))
            response = requests.get(url , params = params)
            print(i + ' is ' + response.text)
    else:
        params = (('MSISDN' , msisdn), ('REQUEST', 'STATUS'))
        response = requests.get(url , params = params)
        print(msisdn + ' is ' + response.text)

    return response.text

def main():
    print('''Make sure the text file submitted is in this format:

CHARGING MSISDN,CHILD MSISDN,SUBSCRIPTION CLASS,CHARGE CLASS,CLIP ID,PRE RBT 
i.e. No spaces after comma
752122295,757383846,CORP,CORP,12345,YES''')
    p1 = input('Press Y to continue or press ctrl + c to exit \n')
    if p1 == 'Y':
        file = open(sys.argv[1] , 'r+')
        lines = file.readlines()
        file.close()
        for i in range(len(lines)):
            lines[i] = lines[i].rstrip('\n')
            lines[i] = lines[i].split(',')
        delay = []
        to_act = {}
        print('The Charging MSISDN is:' + lines[0][0])
        print('The Child MSISDN are :')
        for i in lines:
            text = status_check(i[1])
            if text == 'ACTIVE':
                delay.append(i[1])
            elif text == 'NEW_USER' or 'DEACTIVE':
                to_act[i[1]] = text
            else:
                print('Invalid MSISDN Please Check the file \nTerminating...\n')
                sys.exit()

        if len(delay) != 0:
            print('These are already active')
        print('\n')
        for i in to_act:
            print(i, end = '; ')
        else:
            print('\nThese above numbers will be charged for this Charging MSISDN:' + lines[0][0] +'\n')
            print('The clip ID for the activation is: ' + lines[0][4] + '\n')
            print('These numbers will be charged for '+ lines[0][3])
            p2 = input('If above values are correct Press Y to procede.\n')
            if p2 =='Y':
                for i in lines:
                    if to_act[i[1]] == 'NEW_USER' or 'DEACTIVE':
                        params = (
                            ('MSISDN', i[1]), 
                            ('REQUEST', 'selection'), 
                            ('SELECTED_BY', 'CCC'), 
                            ('TONE_ID', i[4]), 
                            ('CATEGORY_ID', '1'), 
                            ('ISACTIVATE', 'TRUE'), 
                            ('CHARGEMDN', i[0]), 
                            ('CHARGE_CLASS', i[2]),
                            ('SUBSCRIPTION_CLASS', i[3]),
                            ('SELECTIONTYPE', '2'))
                        chrg_resp = requests.get(url , params = params)
                        print(i[1] + ' : ' + chrg_resp.text)

                    else:
                        p3 = input('To Deactivate Press D\n')
                        if p3 == 'D':
                            for i in delay:
                                params = (('MSISDN', i),('REQUEST', 'DEACTIVATE'),('DEACTIVATED_BY', 'CCC'))
                                dct_resp = requests.get(url, params = params)
                        else:
                            print('Exiting..!!')
        print('Checking status\n')
        status_check(to_act)
        
    else:
        print('''You have entered wrong value
Exiting the program...''')



if __name__ == '__main__':
    main()
