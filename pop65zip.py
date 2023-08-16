import re
import sys
import gzip

# find the population of people over 65 per zip code                                                                                                                       
f = open("ACS2018") # this file contains the populations per zip code 
data = f.readline()


while data:
    fields = data.split("|") # this file is pipe delimited 
    field = fields[1] # this field contains the zip code 
    zips = re.match('ZCTA5 ([0-9]{5})', field) # only want the first 5 digits 
    pop65 = fields[327] # this field contans the population for that zip over 65

    if zips:
        print(str(zips.group(1)) + "|" + str(pop65)) # so zipcode | pop

    data = f.readline()
    
f.close()

# put it in file pop65zip with 33121 zips except 20902 zip is repeated twice - so ultimately use 33120 zips 

