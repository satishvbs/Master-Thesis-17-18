#This script reads the list of pdb file and moves the corresponding pdb file in each family
import os
import shutil


current_dir = os.getcwd()
print("Current working directory: "+current_dir)

input_dir = r'E:\Python Thesis\Data-Download\opm\pdb\\'
#out_channel = r'E:\Python Thesis\Data-Download\data\channel_PDB_in_OPM\\'
out_trans = r'E:\Python Thesis\Data-Download\data\transporter_PDB_in_OPM\\'
files = os.listdir(input_dir)
print("Total No of PDB files in OPM database : ", len(files))



'''

#List_Channel = [line.rstrip('\n') for line in open('CHANNEL_PDB_LIST.csv')]
#print("\n"+"Channel PDB LIST:",List_Channel)
#print("No. Of Channel PDB files in mp3struc Database :",len(List_Channel))

for list in List_Channel:
    for pdb in files:
        print(pdb)
        if pdb.startswith(list):
            shutil.copy(os.path.join(input_dir,pdb),out_channel)
        else:
            pass

os.chdir(current_dir)
'''
SW_List_Transporter = [line.rstrip('\n') for line in open('StephenWhite_TRANSPORTERS_LIST.csv')]
print("\n"+"PDB LIST:",SW_List_Transporter)
print("No. Of Channel PDB files in mp3struc Database :",len(SW_List_Transporter))
'''

newList = ''

for list in SW_List_Transporter:
    for pdb in files:
        if pdb.startswith(list):
            shutil.copy(os.path.join(input_dir,pdb),out_trans)
            newList = newList + "\n" + list
        else:
            pass

outfile = open('TRANSPORTERS_LIST_In_OPM.csv', 'w')
outfile.write(newList)
outfile.close()
'''

OPM_List_Transporters = [line.rstrip('\n') for line in open('TRANSPORTERS_LIST_In_OPM.csv')]
print("Number.Of Transporters PDB IDs in StephenWhite Database :",len(SW_List_Transporter))
print("Number.Of Transporters PDB IDs in OPM Database :",len(OPM_List_Transporters))

newList = ''
b=0
for id in SW_List_Transporter:
    if id in OPM_List_Transporters :
        newList = newList + '\n'+ "Exists          = " + id

    else:
        newList = newList + '\n' + "Does not Exists = " + id
        b=b+1
print("Missing no of files= ",b)
outfile = open('Transporters_CHECK_LIST_In_OPM.csv', 'w')
outfile.write(newList)
outfile.close()
