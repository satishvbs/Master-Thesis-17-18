#This script reads line by line removes the lines and makes alist form the csv file
import csv

lines = [line.rstrip('\n') for line in open('Channel-PDB-ID.csv')]

with open("Channel_List.csv",'w') as resultFile:
    wr = csv.writer(resultFile,dialect='excel')
    wr.writerow(lines)
#print(lines)