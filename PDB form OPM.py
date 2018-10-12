#This script checks the missing PDB ids from in StephenWhte List in OPM DataList.
SW_List_Channel = [line.rstrip('\n') for line in open('raw-channels-pdb-list.csv')]
SW_List_Transporter = [line.rstrip('\n') for line in open('raw-transporters-pdb-list.csv')]
OPM_List = [line.rstrip('\n') for line in open('OPM-PDB-LIST_Oct-1-2018.csv')]
print("Number of PDB in OPM DATABASE:",len(OPM_List),'\n')
OPM_List_Channel = [line.rstrip('\n') for line in open('OPM_Channel_LIST.csv')]
print("Number.Of Channel PDB IDs in StephenWhite Database :",len(SW_List_Channel))
#print("Number.Of Channel PDB IDs in OPM Database :",len(OPM_List_Channel))
print('\n')



#print("Number.Of Transporter PDB IDs in StephenWhite Database :",len(SW_List_Transporter))
#print("Number.Of Channel PDB IDs in OPM Database :",len(OPM_List_Channel))



newList1 = ''
for id in SW_List_Channel:
    if id in OPM_List_Channel:
        newList1 = newList1 + '\n' + id
        print(newList1)
    else:
        newList1 = newList1 + '\n'  + id + "\t"+ "NA "

print(newList1)

'''
outfile = open('Channel_CHECK_LIST_In_OPM.xls', 'w',encoding="utf-8")
outfile.write(newList)
outfile.close()

'''
'''
newList2 = ''
for id in SW_List_Transporter:
    if id in OPM_List:
        newList2 = newList2 + '\n' + id
        print("Exist",newList2)
    else:
        newList2 = newList2 + '\n'  + id + "\t"+ "NA "

print(newList2)



outfile = open('Transporters_CHECK_LIST_In_OPM.xls', 'w',encoding="utf-8")
outfile.write(newList2)
outfile.close()

'''