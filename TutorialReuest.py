#This script checks the missing PDB ids from in StephenWhte List in OPM DataList.
SW_List_Channel = [line.rstrip('\n') for line in open('StephenWhite_CHANNEL_LIST.csv')]
OPM_List_Channel = [line.rstrip('\n') for line in open('OPM_Channel_LIST.csv')]
print("Number.Of Channel PDB IDs in StephenWhite Database :",len(SW_List_Channel))
print("Number.Of Channel PDB IDs in OPM Database :",len(OPM_List_Channel))

newList = ''
b=0
for id in SW_List_Channel:
    if id in OPM_List_Channel:
        newList = newList + '\n'+ "Exists          = " + id
        #print("Exists =",newList)
    else:
        newList = newList + '\n' + "Does not Exists = " + id
        b = b+1


print("No.Of missing files = ",b)
print(newList)

outfile = open('Channel_CHECK_LIST_In_OPM.csv', 'w')
outfile.write(newList)
outfile.close()
