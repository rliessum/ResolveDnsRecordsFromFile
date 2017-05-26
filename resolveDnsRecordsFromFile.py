#! /usr/bin/env python3
import csv
import os
import sys
import socket
import dns.resolver
import datetime
import pprint
from tabulate import tabulate

# 18092016 RvL: Play around app, utility to resolve DNS A records from a file
# 19092016 RvL: Some file handling tweaks

def main():
    # Run multiple functions under main
    # readAndResolveFromFile()
    # readAndResolveFromFileTable()
    return

def get_script_path(for_file = None):
    path = os.path.dirname(os.path.realpath(sys.argv[0] or 'something'))
    return path if not for_file else os.path.join(path, for_file)

def readAndResolveFromFile():
     
    #fileName = "c:\\tmp\\dev\\ResolveDnsRecordsFromFile-master\\dnsInput.csv"
    #fileNameOut = "c:\\tmp\\dev\\ResolveDnsRecordsFromFile-master\\dnsInput-output.csv"
    #fileName = ("dnsInput.csv")    
    fileName = ("/Users/richard/Documents/VisualStudio/WorkDev/resolveWithDNS/dnsInput.csv")    
    fileNameOut = ("/Users/richard/Documents/VisualStudio/WorkDev/resolveWithDNS/dnsInput-output.csv")
    try:
        with open((fileName),"r") as fileInput:
            fileFound = True
    
    except FileNotFoundError:
        print("Could not locate file " + fileName)
        fileFound = False

    #  Other errors could occur, perhaps the file is coorupte, or I do not have permissions on the file
    except:
        error = sys.exc_info()
        print(error)
        fileFound = False
    
    if  fileFound:
        with open((fileName),"r") as fileInput:
            fileFound = True
            allRowsList = csv.reader(fileInput)
            data = list(allRowsList)
            row_count = len(data)
            print("File used for input is %s" % fileName)
            print("File used for output is %s" % fileNameOut)
            print("-" * 50)
            print("There are %s rows in this file" % row_count)
            print("-" * 50)
            print("FileName location is %s:\n" % (get_script_path(fileName)))
            print("-" * 50)
            
#for index in range(len(data)):
#    for row in data:
#        print("-" * 20)
#        print(data[index])
#        headers = ["Result","IP"]
#        table = data
#        print(tabulate(table, headers, tablefmt="grid"))

    for currentRow in data :
        for currentWord in currentRow :
          print(",".join(currentRow))
          myResolver = dns.resolver.Resolver()
          myAnswers = myResolver.query((currentWord), "A")
          for outputRecord in myAnswers:
              print("%s\n" % (outputRecord))
              #with open((fileNameOut), 'w', newline='') as fileNameOutCSV:
              #    writer = csv.writer(fileNameOutCSV, delimiter =',')
              #    writer.writerows(outputRecord)
              #    writer.close()()
    
#    spamwriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
#    spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
#    spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])
          date = datetime.datetime.now().strftime("date-%Y-%m-%d_time-%H-%M-%S")
          fileNameOut = "dnsoutput"
          with open((fileNameOut)+'_'+(date)+'.csv', 'a', newline='') as csvfile:
              csvwriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
              outputRecordList = list()
              outputRecordList.append(currentRow)
              print(",".join(currentRow))
              myResolver = dns.resolver.Resolver()
              myAnswers = myResolver.query((currentWord), "A")
          for outputRecord in myAnswers:
              with open((fileNameOut)+'_'+(date)+'.csv', 'a', newline='') as csvfile:
                  csvwriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                  print("%s\n" % (outputRecord))
                  outputRecordList.append(outputRecord)
                  print ("Updated List with record %s" % (outputRecordList))
                  csvwriter.writerow(outputRecordList)


def readAndResolveFromFileTable():
    fileName = input("Provide a CSV as input [file.csv] ")  
    #fileName = "/Users/richard/Documents/VisualStudio/WorkDev/resolveWithDNS/dnsInput.csv" # for testing, static input
    with open((fileName),"r") as fileInput :
        allRowsList = csv.reader(fileInput)
        data = list(allRowsList)
        row_count = len(data)
        print("File used for input is %s\n" % fileName)
        print("There are %s rows in this file\n" % row_count)

#for index in range(len(data)):
#    for row in data:
#        print("-" * 20)
#        print(data[index])
#        headers = ["Result","IP"]
#        table = data
#        print(tabulate(table, headers, tablefmt="grid"))

    for currentRow in data :
      for currentWord in currentRow :
           #print(",".join(currentRow))
           myResolver = dns.resolver.Resolver()
           myAnswers = myResolver.query((currentWord), "A")
           for outputRecord in myAnswers:
               #print("%s\n" % (outputRecord))
                headers = ["Result","IP"]
                table = [(myAnswers),(currentRow)]
                print(tabulate(table, headers, tablefmt="grid"))

#main()

tableOptions = input("Do you the output in tables [yes/no] ").upper()

if tableOptions == ("YES"):
    print("Format with tables")
    readAndResolveFromFileTable()
elif tableOptions == ("NO"):
    print("Format without tables")
    print("-" * 50)
    readAndResolveFromFile()
else:
    print("No selection has been made!")
