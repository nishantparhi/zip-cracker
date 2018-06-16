#!/usr/bin/python2
# zip-cracker author: NISHANT PARHI
# This program is meant to be run with Python Version 2
# usage: python zipcracker.py -f <zipfile> -d <dictionary file>

from zipfile import ZipFile
import optparse
import os
from threading import Thread

def extractFile(zFile, password):
    try:
        zFile.extractall(pwd=password)
        print(('[+] Found Password: ' + password))
    except:
        pass

def main():
    parser= optparse.OptionParser("usage" + "-f <zipfile> -d <dictionary>")
    parser.add_option('-f', dest='zname', type='string', help='specify zip file')
    parser.add_option('-d', dest='dname', type='string', help ='speficy dictionary file')
    (options, args) = parser.parse_args()
    if (options.zname==None) | (options.dname==None):
        print((parser.usage))
        exit(0)
    else:
        zname = options.zname
        if(os.path.isfile(zname)):
            dname = options.dname
            if(os.path.isfile(dname)):
                zFile = ZipFile(zname)
                passFile = open(dname)
                for line in passFile:
                    password = line.strip('\n')
                    t = Thread(target=extractFile, args=(zFile, password,))
                    t.start()
            else:
                print("ERROR: invalid dictionary")
        else:
            print("ERROR: invalid zip archive")


if __name__ == '__main__':
    main()
