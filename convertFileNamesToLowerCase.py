#This script reads the list of pdb file and moves the corresponding pdb file in each family
import os
import shutil
import pathlib


current_dir = os.getcwd()
print("Current working directory: "+current_dir)

#input_dir = r'E:\Python Thesis\Data-Download\opm\pdb\\'
input_dir = r'E:\Python Thesis\Data-Download\data\channel_PDB_in_OPM\\'
#out_trans = r'E:\Python Thesis\Data-Download\data\transporter_PDB_in_OPM\\'
files = os.listdir(input_dir)
print("Total No of PDB files in OPM database : ", len(files))


List_Channel = [line.rstrip('\n') for line in open('CHANNEL_PDB_LIST.csv')]
print("\n"+"Channel PDB LIST:",List_Channel)
print("No. Of Channel PDB files in mp3struc Database :",len(List_Channel))
newList = ''


for list in List_Channel:
    for pdb in files:
        if pdb.startswith(list) :
            newList =newList+"\n"+list

outfile = open('ChannelLIST_In_OPM.csv', 'w')
outfile.write(newList)
outfile.close()



