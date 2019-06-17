import requests as rq
import os
import sys

url = 'http://172.27.102.56:8080/rbt/rbt_promotion.jsp'

def file_read(file_name):
    file = open(file_name, 'r+')
    lines = file.readlines()

    for i in range(len(lines)):
        lines[i] = lines[i].rstrip('\n')
        lines[i] = lines[i].split(',')
    return lines


def get_msisdn(lines):
    msisdn = []
    for i in lines[1:]:
        msisdn.append(i[1])
    return msisdn



lines = file_read(sys.argv[1])
msisdn = get_msisdn(lines)
delay = [i for i in msisdn if rq.get(url, params = (('MSISDN', i),('REQUEST','STATUS'))).text == 'ACTIVE']

def status():
    for i in msisdn:
        param = (('MSISDN', i),('REQUEST','STATUS'))
        response = rq.get(url , params = param)
        print(i + ' : ' + response.text)
    print(str(len(msisdn)) + ' Numbers\n')
#        if response.text == 'ACTIVE':
#            delay.append(i)
#    return delay


def call_function(arg):
    fn_switch = {'0': status, '1': deactivate, '2': activate, '3': disable_prerbt, '4': check_db}
    func = fn_switch.get(arg, lambda: "\n\n INVALID CHOICE!!!!\n\n")
    print(func())


def check_db():
    db_sub = os.popen('''mysql -uroot -ponmobile rbt -e "select subscriber_id, subscription_yes, start_date, subscription_class from rbt_subscriber where subscriber_id in %s order by subscription_class ;" ''' %str(tuple(msisdn))).readlines()

    query = ''' select subscriber_id, subscriber_wav_file, sel_status, set_time from rbt_subscriber_selections where subscriber_id in %s and sel_status='B' order by subscriber_wav_file; ''' % str(tuple(msisdn))
#    print(query + '\n')
    db_sel = os.popen('''mysql -uroot -ponmobile rbt -e " %s " ''' %query ).readlines()
    print('\nSubscribers Table\n')
    for i in db_sub:
        print(i.rstrip('\n'))
    print('\n\n\nSelections Table\n')
    for i in db_sel:
        print(i.rstrip('\n'))


def selection():
    for i in msisdn:
        params = (
                    ('MSISDN', i[1]),
                    ('REQUEST', 'SELECTION'),
                    ('SUB_TYPE', 'P'),
                    ('TONE_ID', i[2]),
                    ('SELECTED_BY', 'CCC'),
                    ('CATEGORY_ID', '1'),
                    ('ISACTIVATE', 'TRUE'),
                    ('SUBSCRIPTION_CLASS', 'CORP'),
                    ('CHARGE_CLASS', 'CORP'),
                    ('IN_LOOP', 'TRUE'),
                    )
        response = rq.get(url , params = params)
        print( i[1] + ' : ' + response.text)


def get_data_from_excel(file_name):
    file = open(file_name, 'r+')
    lines = file.readlines()

    for i in range(len(lines)):
        lines[i] = lines[i].replace('\xa0\t', '\t')
        lines[i] = lines[i].rstrip('\n')
        lines[i] = lines[i].split('\t')

    return lines



def activate():
    for i in lines[1:]:
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
                 ('SELECTIONTYPE', '2'),
                 )
        act_response = rq.get(url, params = params)
        print(i[1] + ' : ' + act_response.text)


def deactivate():
    os.popen('''mysql -uroot -ponmobile rbt -e "delete from rbt_subscriber_downloads where subscriber_id in %s and download_status='y' ;" ''' %str(tuple(msisdn))
    for i in delay:
        params = (
             ('MSISDN', i),
             ('REQUEST', 'DEACTIVATE'),
             ('DEACTIVATED_BY', 'CCC'),
                )
        dct_response = rq.get(url , params = params )
        print(i + ' : ' + dct_response.text)


def disable_prerbt():
    for i in lines[1:]:
        if i[5] == 'YES':
            params = (
            ('isPressStarIntroEnabled', 'n'),
            ('isPostMethod', 'n'),
            ('subscriberID', i[1]),
            ('useSameResForConsent', 'n'),
            )
            disrbt_response = rq.post('http://172.27.102.56:8080/rbt/SetSubscriberDetails.do', params = params)
            if 'SUCCESS' or 'success' in disrbt_response.text:
                print(i[1] + ' : ' + 'SUCCESS')
            else:
                print(i[1] + ' : ' + 'FAILED')


def main():
    value = 'y'
    while value == 'y':
        choice = input('0: Check Status of the numbers.\n1: Deactivate the ACTIVE numbers.\n2: Activate the numbers.\n3: Disable the Pre-RBT.\n4: Check in Database.\n5: Exit\nEnter you choice: ')
        if choice == '5':
            break
        else:
            call_function(choice)
        value = input('Press \'x\' to exit or \'y\' to continue Operations:  ')
        if value == 'x':
            break




#-----Boiler Plate-----
if __name__=='__main__':
    main()
