import re
import sys
import gzip

f = gzip.open("medDrugs2017.gz", "rt") # open the medicare data with information on the each npi's prescribed drugs 
data = f.readline()
table_pat = re.compile(
    r'(DONEPEZIL|RIVASTIGMINE|GALANTAMINE|MEMANTINE)', # these are the drugs given to treat dementia                                                                                     
    flags=re.DOTALL # So that the . character consumes newlines too                                                                                                                                
)

npi = {}    # to keep track of the doctors who prescribed dementia drugs                                                                                                                           

while data:

    fields = data.split("\t") # the file is tab delimited 

    #find all of the doctors who prescribed Dementia Drugs                                                                                                                                         
    table = re.findall(table_pat, fields[8])
    data = f.readline()

    # add all of the npis of doctors who prescribed Dementia drugs to a dictionary with the data being the total days supply prescribed by the dr
    if table:
        if fields[0] in npi:
            npi[fields[0]] += int(fields[12])
        else:
            npi[fields[0]] = int(fields[12])

f.close()

# go through the dictionary and print the results (the npi with the total of total days supply they prescibed
for dr in npi:
    print(str(dr) + "|" + str(npi[dr]))

