#!/usr/bin/python3
# File finder any consolidator
import os, sys, shutil
def collect(format):
    foldername = format.capitalize()
# Making Directory as the format name
    os.mkdir((os.curdir) + '/' + foldername)
    file_loc = os.popen('find . -name "*.%s"'%format).readlines()
    filename = os.popen('ls -R | grep "\.%s"'%format).readlines()
# Copying all the files found to the directory
    for i in range(0,len(file_loc)):
        shutil.copyfile(file_loc[i].rstrip('\n'), foldername + '/' + filename[i].rstrip('\n'))
# Getting the file name
    os.chdir(foldername)
    file_count = os.popen('ls | wc -l').readlines()
    print(file_count[0] + 'Files copied successfully')
    files = (os.popen('ls').readlines())
    for i in range(0,len(files)):
        print(files[i].rstrip('\n'))

def main():
    if len(sys.argv) == 1:
        print('Please Enter the format keyword like this xml, jar, mp3, mp4, jpg, properties')
    format = sys.argv[1]
    collect(format)


#-----Boiler Plate-----
if __name__=='__main__':
    main()
