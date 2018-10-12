#This script is to list the missing pdb Id inn OPM data base

import os


current_dir = os.getcwd()
print("Current working directory: "+current_dir)

input_channel= r'E:\Python Thesis\Data-Download\data\Channels\\'

out_channel= r'E:\Python Thesis\Data-Download\data\Channels\\'

input_trans= r'E:\Python Thesis\Data-Download\data\Transporters\\'
out_trans= r'E:\Python Thesis\Data-Download\data\Transporters\\'



##########################################
#for Channles
files_channel = os.listdir(input_channel)

List_Channel = [line.rstrip('\n') for line in open('Channel-PDB-ID.csv')]
print("No. Of Channel PDB files in mp3struc Database :", len(List_Channel))
print("No os Channels structure in OPM Database: ",len(files_channel))
print("\n"+"Channel PDB LIST:",List_Channel)

ss = set(List_Channel)
fs = set(files_channel)
missing_channel_pdb = fs.intersection(ss)
#missing_channel_pdb = ss.union(fs) - c

print("Missing PDB Ids are: ",missing_channel_pdb)
print("No of missing files= ", len(missing_channel_pdb))


#print(set(List_Channel) & set(files_channel))
print()
#for x in missing_channels:
    #print(x)

os.chdir(current_dir)

###############################################################

#For transporters
files_Transporter= os.listdir(input_trans)
List_Transporter = [line.rstrip('\n') for line in open('List_Transporter.csv')]
#print("\n"+"PDB LIST Transporter:",List_Transporter)
#print("No. Of Transporter PDB files in mp3struc Database :",len(List_Transporter))
#print("No os Transporter structure in OPM Databse: ",len(files_Transporter))

'''

works:

-------------------------------
Missing Pdb IDs
-------------------------------
#List_Channel = ['1anx.pdb','1atx.pdb','1auv.pdb','1aou.pdb']
#files_channel = ['bly.pdb','2zba.pdb','1atx.pdb','1auv.pdb','1aou.pdb','bly.pdb','2zba.pdb']
ss = set(List_Channel)
fs = set(files_channel)
missing_channel_pdb = ss.union(fs) - ss.intersection(fs)

List_Channel = [line.rstrip('\n') for line in open('List_channel.csv')]
print("\n"+"Channel PDB LIST:",List_Channel)
print("No. Of Channel PDB files in mp3struc Database :",len(List_Channel))

List_Transporter = [line.rstrip('\n') for line in open('List_Transporter.csv')]
print("\n"+"PDB LIST:",List_Transporter)
print("No. Of Channel PDB files in mp3struc Database :",len(List_Transporter))

opm_list = [line.rstrip('\n') for line in open('List_OPM.csv')]
print("\n"+"OPM LIST",opm_list)
print("No. Of PDB files in OPM_Database :",len(opm_list))




######################################
'''