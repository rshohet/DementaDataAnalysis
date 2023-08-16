import sys

f = open("finalRatio") # this file contains the y-axis of drugs per day per Dementia prevalence
data = f.readline()

yAxis = {} # store the final ratios for the y axis - the drugs days / Dementia cases 

while data:
    fields = data.split("|") # the file is pipe delimited 
    county = fields[0]
    drugsDemPrev = fields[1].strip("\n")

    yAxis[county] = drugsDemPrev

    data = f.readline()

f.close()

f = open("countyIncome") # this file contains the x-axis of average income per county
data = f.readline()

while data:
    fields = data.split("|") # the file is pipe delimited 
    county = fields[0]
    income = fields[1].strip("\n")
    
    # check if the county is in the y-axis points - we need only the counties that we have data for both the income and the drug/dementia prevalence
    if county in yAxis:
        print(county + "|" + str(income) + "|" + str(yAxis[county]))

    data = f.readline()

f.close
