import re
import sys
import gzip

g = open("pop65zip") # this file containts the population over 65 per zip
data1 = g.readline()

zips = {}

while data1:
    field = data1.split("|") # the file is pipe delimited 
    zips[field[0]] = field[1].strip("\n")
    data1 = g.readline()
    
g.close()

f = open("zipCountyConversion") # this file we made contains the conversion between zip and county/state and only includes zips that prescribed Dementia Drugs, which is all we need 
data = f.readline()

countyPop = {}  # keep track of the population over 65 per county -- convert the zips to counties with data being the population over 65                                   
while data:
    fields = data.split("|") # the file is pipe delimited 
    z = fields[0] # zip code is in the first field 
    countyState = fields[1].strip("\n")

    # go through all of the zips from the dictionary where zip is key and population over 65 is data                                                                       
    for i in zips:
       
        # if the zip is in the conversion table, find its county in 6th field and add it to dictionary of counties with key being population over 65 of that county       
        if z == i:
            if countyState in countyPop:
                countyPop[countyState] += int(zips[i])
            else:
                countyPop[countyState] = int(zips[i])

    data = f.readline()

f.close()

#found 1907 different counties with their population over 65 
for county in countyPop:
    print(county + "|" + str(countyPop[county]))
