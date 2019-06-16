#!/usr/bin/python3
import os

def call_function(arg):
    fn_switch = {'0': status, '1': deactivate, '2': activate, '3': pre_rbt_disable}
    func = fn_switch.get(arg, lambda: "\n\n INVALID CHOICE!!!!\n\n")
    print(func())


def status():
    print('Status')
    print('Checking the status...\n')

def deactivate():
    print('Deactivating')
    print('Deactivating the numbers...\n')

def activate():
    print('Activating')
    print('Activating the numbers...\n')

def pre_rbt_disable():
    print('Disabling Pre-RBT')
    print('Disbaling the Pre-RBT...\n')


def main():
    value = 'y'
    while value == 'y':
        choice = input('0: Check Status of the numbers.\n1: Deactivate the numbers.\n2: Activate the numbers.\n3: Disable the Pre-RBT.\nEnter you choice: ')
        call_function(choice)
        value = input('Press \'x\' to exit or \'y\' to continue Operations:  ')
        if value == 'x':
            break


            

#-----Boiler Plate-----
if __name__=='__main__':
    main()
