#!/usr/bin/env python3
import csv
import os
import sys
import datetime
#import dns.resolver
import dns.resolver
import terminaltables

FILENAME = "dnsInput.csv"


def main():
    tableOptions = input('Do you the output in tables [Y/N]').upper()

    if tableOptions == ('Y'):
        print('Format with tables')
        read_and_resolve_from_filetable()
    elif tableOptions == ('N'):
        print('Format without tables')
        print('-' * 50)
        read_and_resolve_from_file()
    else:
        print('No selection has been made!')


def get_script_path(for_file = None):
    path = os.path.dirname(os.path.realpath(sys.argv[0] or 'something'))
    return path if not for_file else os.path.join(path, for_file)


def read_and_resolve_from_file():
    fileName = FILENAME
    #fileName = input('Provide a CSV as input [file.csv] ')
    fileNameOut = ('dnsOutput.csv')
    try:
        with open(FILENAME) as file:
            fileFound = True
            pass
    except IOError as e:
        print("Unable to open file")

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
            with open((fileNameOut)+'_'+(date)+'.csv', 'a', newline='') as csvfile:
                csvwriter = csv.writer(csvfile, delimiter=' ', quotechar='|',
                                       quoting=csv.QUOTE_MINIMAL)
                outputRecordList = list()
                outputRecordList.append(currentRow)
                (','.join(currentRow))
                myResolver = dns.resolver.Resolver()
                myAnswers = myResolver.query((currentWord), 'a')
            for outputRecord in myAnswers:
                with open((fileNameOut)+'_'+(date)+'.csv', 'a', newline='') as csvfile:
                    csvwriter = csv.writer(csvfile, delimiter=',', quotechar='|',
                                           quoting=csv.QUOTE_MINIMAL)
                    outputRecordList.append(outputRecord)
                    print('\n'.join(str(p) for p in outputRecordList))
                    csvwriter.writerow(outputRecordList)


def read_and_resolve_from_filetable():
    fileName = input('Provide a CSV as input [file.csv] ')
    with open((fileName),'r') as fileInput :
        allRowsList = csv.reader(fileInput)
        data = list(allRowsList)
        row_count = len(data)
        print('File used for input is %s\n' % fileName)
        print('There are %s rows in this file\n' % row_count)

    for currentRow in data :
      for currentWord in currentRow :
           #print(','.join(currentRow))
           myResolver = dns.resolver.Resolver()
           myAnswers = myResolver.query((currentWord))
           for outputRecord in myAnswers:
                print('%s\n' % (outputRecord))
                headers = ['Result','IP']
                table = [(myAnswers), (currentRow)]
                #print(tabulate(table, headers, tablefmt='grid'))


if __name__ == "__main__":
    main()