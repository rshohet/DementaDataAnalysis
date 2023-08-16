import re
import sys
import gzip

f = open('50States.txt') # this file contains states and their abbreviations which we need since all the other data has state abbrv but this data has the full name
data = f.readline()

states = {}

while data:
    newData = re.sub(r'([\s]{2,}|\t)', "|", data) # some are tab delimited and some just have multiple spaces, so replace either with a pipe
    fields = newData.split("|") # file is tab delimited
    name = fields[0] # state name in first field
    abbrv = fields[1] # abbrevation in second field

    states[name] = abbrv # the key is the state and the data is the abbreviation 

    data = f.readline()

f.close()

f = open("County_Prevalence_2017.txt") # this data contains the prevalence of diseases, like Dementia
data = f.readline()

while data:
    fields = data.split("\t") # the data is tab delimited 
    state = fields[0].strip() # state is the first field 
    county = fields[1].strip() # county is the second field 
    pat = re.search(r'[0-9\.]*', fields[4]) # some prevalence have * and no data, so don't include those
    prevDem = pat.group(0)

    if county and state and prevDem: # as long as the fields have data
        state = states[state] # the abbrevation 
        countyState = county + "/" + state 
        
        print(countyState + "|" + str(prevDem))

    data = f.readline()

f.close()


