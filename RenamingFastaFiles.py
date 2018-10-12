#This script is to rename the fasta file adding-pdb id wiht their UniprotID


import os

current_dir = os.getcwd()
print("Current working directory: "+current_dir)

input_dir = r'C:\Users\satis\Desktop\InputFastaFiles\\'
output_dir = r'E:\Python Thesis\Data-Download\renamed-FastaFiles\\'

files =os.listdir(input_dir)
print("Total No of files = ",len(files))


rename = ''
for fastaFile in files:
    os.chdir(output_dir)
    #print("FastaFile= ",fastaFile)
    pdb_id = fastaFile[0:4]
    #print("PDB ID = ",pdb_id)
    lines = open(input_dir+fastaFile).readlines()
    print("Processing : %s" % fastaFile)
    outlines = ''
    sequence = ''
    for line in lines:

        if line.startswith('>'):
            begining = line[0:10]
            rename = begining +'-'+pdb_id + '|' + line[11:]
            outlines = outlines+rename
        elif not line.startswith('>'):
            sequence = sequence + line
    outlines = outlines + sequence
    print(outlines)


    outfile = open(fastaFile, 'w')
    outfile.write(outlines)
    outfile.close()



