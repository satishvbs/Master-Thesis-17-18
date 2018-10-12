
'''
with open('Channel-PDB-ID.csv') as f:
    for line in f:
# you may also want to remove whitespace characters like `\n` at the end of each line
        content = [x.rstrip('\n') for x in line]
        print(content)
'''


