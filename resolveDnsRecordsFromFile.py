#!/usr/bin/env python3
import csv
import os
import sys
import datetime
import dns.resolver

FILENAME = "dnsInput.csv"


def main():
    read_and_resolve_from_file()


def get_script_path(for_file=None):
    path = os.path.dirname(os.path.realpath(sys.argv[0] or 'something'))
    return path if not for_file else os.path.join(path, for_file)


def read_and_resolve_from_file():
    fileName = FILENAME
    fileNameOut = ('dnsOutput.csv')
    try:
        with open(FILENAME) as file:
            fileFound = True
            pass
    except IOError as e:
        print('Unable to open file')

    if fileFound:
        with open((fileName), 'r') as fileInput:
            fileFound = True
            allRowsList = csv.reader(fileInput)
            data = list(allRowsList)
            row_count = len(data)
            print('File used for input is %s' % fileName)
            print('File used for output is %s' % fileNameOut)
            print('-' * 100)
            print('There are %s rows in this file' % row_count)
            print('-' * 100)
            print('FileName location is %s:' % (get_script_path(fileName)))
            print('FileName location is %s:' % (get_script_path(fileNameOut)))
            print('-' * 100)

    for currentRow in data:
        for currentWord in currentRow:
            (','.join(currentRow))
            myResolver = dns.resolver.Resolver()
            myAnswers = myResolver.query((currentWord))
            date = datetime.datetime.now().strftime('date-%Y-%m-%d_time-%H-%M-%S')
            fileNameOut = 'dnsoutput'
            with open((fileNameOut)+'_'+(date)+'.csv', 'a') as csvfile:
                csvwriter = csv.writer(csvfile, delimiter=' ', quotechar='|',
                                       quoting=csv.QUOTE_MINIMAL)
                outputRecordList = list()
                outputRecordList.append(currentRow)
                (','.join(currentRow))
                myResolver = dns.resolver.Resolver()
                myAnswers = myResolver.query((currentWord), 'a')
            for outputRecord in myAnswers:
                with open((fileNameOut)+'_'+(date)+'.csv', 'a') as csvfile:
                    csvwriter = csv.writer(csvfile, delimiter=',', quotechar='|',
                                           quoting=csv.QUOTE_MINIMAL)
                    outputRecordList.append(outputRecord)
                    newList = str(outputRecordList).replace('[','').replace(']','').replace('\'','').replace(' <DNS IN A rdata: ','').replace('<','').replace('>','')
                    filter = list(outputRecordList[0]) 
                    print(newList)
            with open((fileNameOut)+'_'+(date)+'.csv', 'a') as csvfile:
                csvfile.write("%s\n" % newList)
            

if __name__ == "__main__":
    main()