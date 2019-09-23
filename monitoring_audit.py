import csv
import os
import logging

def main():
    LOG_FORMAT = "%(levelname)s,%(asctime)s - %(message)s"
    logging.basicConfig(filename = 'audit_log.txt' , level = logging.INFO , format = LOG_FORMAT)
    logger = logging.getLogger()

    file_name = input('Enter the filename of monitoring dump:\n')
    field , rows = [], []
    with open(file_name , 'r+') as f:
        csvreader = csv.reader(f)
        field = csvreader.__next__()
        rows = [ i for i in csvreader]
    uniq = ['/Product/Zabbix', '/Product/MSearch', '/Product/RBT TP', '/Product/RBT Player DB', '/Product/RBT DB']
    
    new_rows = [i for i in rows if i[-5] in uniq]
    logger.info("Sheet Sorted Successfully")
    new_filename = 'sorted_excel_sheet.csv'

    with open(new_filename , 'w+') as file:
        csvwriter = csv.writer(file)
        csvwriter.writerow(field)
        csvwriter.writerows(new_rows)

    logger.info("File {0} is Created Successfully".format(new_filename))
    filename = 'URL.csv'
    url_rows = [i for i in rows if 'URL' in i[7]]
    logger.info('URLs Collected')
    with open(filename, 'w+') as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(field)
        csvwriter.writerows(url_rows)
    
    logger.info("File with URLs {0} is created Successfully.".format(filename))
    if new_filename and filename in os.listdir():
        print('Files Created Successfully')
    print(os.listdir())


if __name__ == '__main__':
    main()
