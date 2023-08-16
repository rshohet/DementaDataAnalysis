import sys
import gzip

f = gzip.open('IncomePop.gz', 'rt') # this file contains zip codes and mean income                                                                                                            
data = f.readline()

zips = {} #keep track of the zip codes and their average income 

while data:
    fields = data.split("|") # the file is pipe delimited
    z = fields[0] 
    income = fields[2] 
    zips[z] = income
    data = f.readline()

f.close()

f = open("zipCountyConversion")
data = f.readline()

county = {} # keep track of the county and its average income

while data:
    fields = data.split("|") # the file is pipe delimited 
    zc = fields[0]
    countyState = fields[1].strip("\n")

    # go through all of the zips from the dictionary where zip is key and income is data                                                                                                                   
    for i in zips:

        # if the zip is in the conversion table, find its county and add it to dictionary of counties with key being the county and data being all of the mean incomes of the zips of the county           
         if i == zc:                                                                                                                                                                                       
            if countyState in county: # if we already added that county to our dictionary                                                                                                                  
                county[countyState].append(zips[zc])
            else:
                county[countyState] = [zips[zc]]

    data = f.readline()

f.close()

# go through the counties with the data being a list of the incomes of each zip code in the county 
for c in county:
    numZips = len(county[c]) # this stores the number of zip codes per that county 
    sum = 0 # this will be the average incomes of each zip code in the county added together 

    for inc in county[c]:
        if inc == ".": # there is some data that is just a . so dont include it and make sure change the number of zips used                                                                               
            inc = 0
            numZips -= 1
        sum += int(inc)
    mean = sum / numZips # the mean income is the sum of all the average incomes of each zip code in the county divided by the number of zip codes

    print(c + "|" + str(mean))
