import os

input_folder = r'E:\Python Thesis\Data-Download\DEMo-Uniprot-seq file\\'

files = os.listdir(input_folder)
print("Total no of files=",len(files))

for f in files:
    for line in open(input_folder+f).readlines():
        outlines = " "
        #print(line)

        outlines +=  line
        print(outlines)
        outfile = open("Cluster-Input-Transporter.fasta","w")
        outfile.write(outlines)
        outfile.close()

