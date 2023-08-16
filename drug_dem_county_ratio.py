import sys

f = open('drugsPopCountyRatio')  # this has the ratio of dementia drugs to the population over 65 per county 
data = f.readline()

drugPrev = {} # keep track of the ratio of drugs per population over 65 with key being the county 

while data:
    fields = data.split("|") # file is pipe delimited 

    countyState = fields[0]
    prev = fields[1].strip('\n')

    if countyState in drugPrev:
        drugPrev[countyState] += float(prev) # key is county and data is prevalence of Dementia Drugs in that county
    else:
        drugPrev[countyState] = float(prev)

    data = f.readline()

f.close()

# now need to find the drugs per county of population 65+ per the prevalence of Dementia in the population 65+, which will yield the number of drugs per says per the disease cases
f = open('countyDemPrev')
data =	f.readline()

while data:
    fields = data.split("|") # file is pipe delimited 

    countyState = fields[0]
    prevDem = fields[1]
   
    if countyState in drugPrev: # if we know how many drugs per that county
        drug = float(drugPrev[countyState])
        dementia = float(prevDem) / 100 # bc it is in percentage form, so must divide by 100
        if dementia > 0: # bc cannot divide by zero 
            ratio = drug / dementia # find the ratio by dividing the drug per population over 65 by the prevalence of dementia in that population 
            print(countyState + "|" + str(ratio))

    data = f.readline()
    
f.close()
