#!/usr/bin/python3  -tt

import os
import requests
import mysql.connector

def get_msisdn_info(field):

    data_id = os.popen('cut -d, -f%d Base.txt'%(field+1)).readlines()
    for i in range(len(data_id)):
        data_id[i] = data_id[i].rstrip('\n')
    return data_id

def check_status():
# checking status for each number
    
    for i in data_list['charge_id']:

        for_status = (
            ('MSISDN', '%s') %i,
            ('REQUEST', 'STATUS')
                 )


def main():

# Getting data from Base.txt in format
# CHARGING MSISDN, CHILD MSISDN, SUBSCRIPTION CLASS, CHARGE CLASS, CLIP ID, PRE RBT
# 752122295,757383846,CORP,CORP,12345,YES

# Make sure the Base.txt is in the same directory as the script
    data_list = {'charge_id': [], 'child_id': [], 'subs_class': [], 'charge_class': [], 'clip_id': [], 'pre_rbt': []}
    keys = list(data_list)
    for num in range(len(data_list)):
        data_list[keys[num]] = get_msisdn_info(num)






# url = 'http://172.27.102.56:8080/rbt/rbt_promotion.jsp?MSISDN=701890509&REQUEST=STATUS'

    url = '''http://172.27.102.56:8080/rbt/rbt_promotion.jsp'''

    for_activation = (
        ('MSISDN', '702746048'),
        ('REQUEST', 'selection'),
        ('SELECTED_BY', 'CCC'),
        ('TONE_ID', '31121745'),
        ('CATEGORY_ID', '1'),
        ('ISACTIVATE', 'TRUE'),
        ('CHARGEMDN', '702475655'),
        ('CHARGE_CLASS', 'CORP3'),
        ('SUBSCRIPTION_CLASS', 'CORP3'),
        ('SELECTIONTYPE', '2'),
                  )

    for_deactivation = (
        ('MSISDN', '$f[0]'),
        ('REQUEST', 'DEACTIVATE'),
        ('DEACTIVATED_BY', 'CCC'),
                    )

    stat_res = requests.get(url , params=for_status)
    act_res = requests.get(url , params=for_activation)

# List of responses

    response_list = ['ACTIVE','DEACTIVE','SUBSCRIBER_NOT_EXIST','NEW_USER','GRACE','SUSPENDED','GRACE','ACT_PENDING','DEACT_PENDING','SUSPENDED','INVALID','ACT_PENDING'
,'DEACT_PENDING']

    if stat_res.text in 'ACTIVE':

        for_deactivation = (
        ('MSISDN', '%s')%child_id,
        ('REQUEST', 'DEACTIVATE'),
        ('DEACTIVATED_BY', 'CCC'),
                    )

        deact_res = requests.get(url , params=for_deactivation)



