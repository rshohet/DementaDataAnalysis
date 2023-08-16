import re
import sys
import gzip

f = open("county65") # this file has the population over 65 per county 
data = f.readline()

countyPop65 = {}

# add each county/state and their population over 65 to a dictionary 
while data:
    fields = data.split("|") # the file is pipe delimited 
    county = fields[0] # county/state in first field 
    pop65 = fields[1].strip("\n")
    countyPop65[county] = pop65 # the key is the county and data is the population 
    data = f.readline()

f.close()

f = open("drugsPerCounty") # this file contains the drug supply prescribed per county 
data = f.readline()

countyDrugs = {}

# add each county and their Dementia drugs number prescribed to a dictionary 
while data:
    fields = data.split("|") # the file is pipe delimited 
    county = fields[0] # county/state is in the first fields 
    drugs = fields[1].strip("\n")
    countyDrugs[county] = drugs # the key is the county/state and data is the number of drugs prescribed 
    data = f.readline()

f.close()

drugPopCounty = {} # find the ratio of drugs per county (by nature it is regarding population 65+)  to population of the county 65+                                   

for county in countyDrugs:
    if county in countyPop65 and int(countyPop65[county]) > 0: # only consider counties for which  we have info on the population
        drug = int(countyDrugs[county])
        pop65 = int(countyPop65[county])
        ratio = drug / pop65 # divide the supply of drugs per the population over 65 

        print(str(county) + "|" + str(ratio))

