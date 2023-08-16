import re
import sys
import gzip

f = open("zipDrugs") # open the file already created that holds only the zip codes that had Dementia drugs 
data = f.readline()
zips = {}

while data:
    fields = data.split("|") # file is pipe delimited 
    zips[fields[0]] = fields[1] # key is zip and data is how many drugs prescribed                                                                                                                 
    data = f.readline()

f.close()

# create a conversion table with the zips and the county/state associated with it - but only for zips where Dementia Drugs prescribed 
f = gzip.open("ZIPcodes.gz", "rt") # this file contains the zip codes with their associated state and county
data = f.readline()

while data:
    fields = data.split("|")
    z = fields[0]
    county = fields[6]

    # many county names end in county, parish, census area, or borough and the prevalence data omits these words so don't include them so find and split on it
    if county == "City and Borough of Juneau": # this one county does not match the prevalence data or other data in this file - instead should just be Juneau
        county = "Juneau"
    if " County" in county:
        county = county.split(" County")[0]
    if " Census Area" in county:
        county = county.split(" Census Area")[0]
    if " Borough" in county:
        county = county.split(" Borough")[0]
    if " Parish" in county:
        county = county.split(" Parish")[0]
    countyState = county + "/" + fields[5]

    
    # if the zip had Dementia drugs prescibed, find its county in 6th field and state in the 5th field - the data is both fields to make sure counties are unique 
    if z in zips:
        print(str(z) + "|" + countyState)    

    data = f.readline()

f.close()


#the result is 14360 different zips  prescribed Dementia drugs - even though zipDrugs is 14537, this file must be missing a few zipcodes 

