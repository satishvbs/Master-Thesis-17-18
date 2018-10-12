#This script reads the list of pdb file and moves the corresponding pdb file in each family
import os
import shutil


current_dir = os.getcwd()
print("Current working directory: "+current_dir)

input_dir = r'E:\Python Thesis\Data-Download\opm\pdb\\'
out_channel = r'E:\Python Thesis\Data-Download\data\channel_PDB_in_OPM\\'
out_trans = r'E:\Python Thesis\Data-Download\data\transporter_PDB_in_OPM\\'
files = os.listdir(input_dir)
print("Total No of PDB files in OPM database : ", len(files))


List_Channel = [line.rstrip('\n') for line in open('List_channel.csv')]
print("\n"+"Channel PDB LIST:",List_Channel)
print("No. Of Channel PDB files in mp3struc Database :",len(List_Channel))


for list in List_Channel:
    for pdb in files:
        print(pdb)
        if pdb.startswith(list):
            shutil.copy(os.path.join(input_dir,pdb),out_channel)
        else:
            pass

os.chdir(current_dir)

List_Transporter = [line.rstrip('\n') for line in open('List_Transporter.csv')]
print("\n"+"PDB LIST:",List_Transporter)
print("No. Of Channel PDB files in mp3struc Database :",len(List_Transporter))


for list in List_Transporter:
    for pdb in files:
        print(pdb)
        if pdb.startswith(list):
            shutil.copy(os.path.join(input_dir,pdb),out_trans)
        else:
            pass


'''
works:
#input_dir= r'E:\Python Thesis\Data-Download\opm2\pdb\\'
print("changed directory",os.getcwd())
os.chdir(input_dir)
print("changed directory",os.getcwd())
list1 = ['1anx.pdb','1atx.pdb','1auv.pdb','1aou']


for list in list1:
    for pdb in files:
        print(pdb)
        if list !=pdb:
            print(list[0:4], "Not found")
        else:
            #shutil.copy(os.path.join(input_dir,pdb),ouut_dir)
            print(list, " Found and moved")
    a=a+1
    -------------------------------

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