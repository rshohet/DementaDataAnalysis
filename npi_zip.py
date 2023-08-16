import re
import sys
import gzip

f = open("npi_prescribed") # this file contains the NPI numbers already found to have prescribed Dementia drugs 
dataDemNpi = f.readline()

foundNpi = {} # key is npi and data is how many Dementia drugs prescribed 

while dataDemNpi:
    
    fields = dataDemNpi.split("|") # the file is pipe delimited 
    foundNpi[fields[0]] = fields[1].strip("\n") 
    dataDemNpi = f.readline()

f.close()

# match the npi's of doctors who prescribed dementia drugs with their zip codes
          
f = gzip.open("npi.gz", "rt") # this data contains a doctor's npi and zip code 
dataAllNpi = f.readline() 

zipDrugs = {} # keep track of the supply of Dementia drugs prescribed per zip code 

while dataAllNpi:
    fields = dataAllNpi.split("|") # the file is pipe delimited 
    npi = fields[0] # npi is in the first column
    zipcode = fields[32][:5] # zip code zip code is in the 32nd columns - but only want the first 5 digits 

    # if the npi from the conversion file prescribed a dementia drug
    if npi in foundNpi:
        if zipcode in zipDrugs:
            zipDrugs[zipcode] += int(foundNpi[npi]) # the key is the 5-dig zip code and data is number of Dementia drugs prescibed
        else:
            zipDrugs[zipcode] = int(foundNpi[npi])
       
    dataAllNpi = f.readline()
    
f.close()

# did len(zipDrugs) and found 14537 for 5-dig zipcodes- so prescribed dementia drugs in 14537 zips                                                           

# print the contents of the zipDrugs dictionary 
for zipC in zipDrugs:
    print(str(zipC) + "|" + str(zipDrugs[zipC]))

                   
