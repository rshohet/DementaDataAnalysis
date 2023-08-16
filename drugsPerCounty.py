import re
import sys
import gzip

f = open("zipDrugs") # this file contains the zip codes with number of Dementia drug supply prescribed 
data = f.readline()

zips = {} # keep track of the zip codes associated with Dementia drugs 

while data:
    fields = data.split("|") # file is pipe delimited
    zips[fields[0]] = fields[1].strip("\n") # key is zip and data is how many drugs prescribed
    data = f.readline()

f.close()

# convert the zip codes we find associated with dementia drugs to counties using the conversion zip county conversion file we made 
f = open("zipCountyConversion")
data = f.readline()

countyDrugs = {}      # keep track of how many dementia drugs prescribed per county

while data:
    fields = data.split("|")
    z = fields[0]
    countyState = fields[1].strip("\n")
    
    # if the zip prescribed Dementia drugs, find its county/state and add it to dictionary of counties that prescribed Dementia drugs and its key is # of Dementia drugs prescribed
    if z in zips:
        if countyState in countyDrugs:
            countyDrugs[countyState] += int(zips[z]) # key is county and data is drugs per county 
        else:
            countyDrugs[countyState] = int(zips[z]) 
        
    data = f.readline()

f.close()

#the result is 2979 different counties prescribed Dementia drugs 
for county in countyDrugs:
    print(county + "|" + str(countyDrugs[county]))



