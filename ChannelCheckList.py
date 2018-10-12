#This script checks the missing PDB ids from in StephenWhte List in OPM DataList.
sw_List_Channel = [line.rstrip('\n') for line in open('raw-channels-pdb-Sorted-list.csv')]
sw_List_Transporter = [line.rstrip('\n') for line in open('raw-transporters-pdb-Sorted-list.csv')]
opm_List = [line.rstrip('\n') for line in open('OPM-PDB-LIST_Oct-1-2018.csv')]
print("No. of PDB in OPM:",len(opm_List))
OPM_List_Channel = [line.rstrip('\n') for line in open('OPM_Channel_LIST.csv')]
print("Number.Of Channel PDB IDs in StephenWhite Database :",len(sw_List_Channel))


print("Number.Of Transporter PDB IDs in StephenWhite Database :",len(sw_List_Transporter))
#print("Number.Of Channel PDB IDs in OPM Database :",len(OPM_List_Channel))

newList = ''


for id in sw_List_Channel:
    if id in opm_List:
        newList = newList + '\n' + id

    else:
        newList = newList + '\n' + id + "\t"+ "NA "



#print(newList)

#outfile = open('Filter-Channel_NOT Available_In_OPM.xls', 'w',encoding="utf-8")
#outfile.write(newList)
#outfile.close()

newList2 = ''
for id in sw_List_Transporter:
    if id in opm_List:
        newList2 = newList2 + '\n' + id
        #print(newList2)
    else:
        newList2 = newList2 + '\n'  + id + "\t"+ "NA "

print(newList2)

outfile = open('Filter-Transporters_NOT Available_In_OPM.xls', 'w',encoding="utf-8")
outfile.write(newList2)
outfile.close()

