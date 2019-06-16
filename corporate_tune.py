#!/usr/bin/python3  -tt

import os
import sys
import requests
import mysql.connector

# Global variable   url = 'http://172.27.102.56:8080/rbt/rbt_promotion.jsp?MSISDN=701890509&REQUEST=STATUS'

url = '''http://172.27.102.56:8080/rbt/rbt_promotion.jsp'''


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
        print('The Charging MSISDN is:' + lines[0][0])
        print('The Child MSISDN are :')
        for i in lines:
            params = (('MSISDN' , i[1]), ('REQUEST', 'STATUS'))
            response = requests.get(url , params = params)
            if response.text == 'ACTIVE':
                delay.append(i[1])
            print('MSISDN '+ i[1] +' is ' + response.text)
            if len(delay) == 0:
                print('All are new numbers')
            else:
                print('These numbers are active :' + str(delay) + ' \n')
        if len(delay) == 0:
            p2 = input('Procede for Charging Press Y\n')
            if p2 =='Y':
                    params = (
                            ('MSISDN', '702746048'),
                            ('REQUEST', 'selection'),
                            ('SELECTED_BY', 'CCC'),
                            ('TONE_ID', '31121745'),
                            ('CATEGORY_ID', '1'),
                            ('ISACTIVATE', 'TRUE'),
                            ('CHARGEMDN', '702475655'),
                            ('CHARGE_CLASS', 'CORP3'),
                            ('SUBSCRIPTION_CLASS', 'CORP3'),
                            ('SELECTIONTYPE', '2'))

        p2 = input('To Deactivate Press D\n')
        if p2 == 'D':
            for i in delay:
                params = (('MSISDN', i),('REQUEST', 'DEACTIVATE'),('DEACTIVATED_BY', 'CCC'))
                dct_resp = requests.get(url, params = params)
        else:
            print('Exiting..!!')

    else:
        print('''You have entered wrong value
Exiting the program...''')



if __name__ == '__main__':
    main()
