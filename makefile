all: plot.pdf # the final product is to make the plot of the data 
	echo "Everything has been built!"

clean: # remove each of the files produces so that can re-run the project 
	rm npi_prescribed zipDrugs zipCountyConversion drugsPerCounty pop65zip county65 drugsPopCountyRatio countyDemPrev finalRatio countyIncome XandY plot.pdf

# find the npi numbers of the doctors who prescribed Dementia drugs from medDrugs2017.gz data and record it in npi_prescribed 
npi_prescribed: medDrugs2017.gz
	python3 ./npi_num_dem_prescribed.py > npi_prescribed

# convert the npi numbers we found from npi_prescribed to zip codes using npi.gz and record it in zipDrugs - now have the zip codes where Dementia drugs prescribed 
zipDrugs: npi_prescribed npi.gz
	python3	./npi_zip.py > zipDrugs

# convert the zip codes associated with Dementia drugs to counties using the zipDrugs file and the ZIPcodes.gz conversion file and store in zipCountyConversion
zipCountyConversion: zipDrugs ZIPcodes.gz
	python3 ./zip_to_county.py > zipCountyConversion

# find the total number of supply prescribed per county using zipDrugs which has the total of the days supply per zip code and using the zipCountyConversion and record in drugsPerCounty
drugsPerCounty: zipDrugs zipCountyConversion
	python3 ./drugsPerCounty.py > drugsPerCounty

# find the population over 65 per zip code using data file ACS2018 and record it in pop65zip
pop65zip: ACS2018
	python3 ./pop65zip.py > pop65zip

#  find the population over 65 per county using pop65zip which has the population over 65 per zip code and using the zipCountyConversion table and record it in county65 
county65: pop65zip zipCountyConversion
	python3 ./popZip_to_county.py > county65

# find the ratio of drugs per population over 65 per county by dividing the total drug days by the pop over 65 using county65 and drugsPerCounty and record the ratio in drugsPopCountyRatio
drugsPopCountyRatio: county65 drugsPerCounty
	python3 ./drugs_pop_county_ratio.py > drugsPopCountyRatio

# find the prevalence of Dementia per county from the County_Prevalence_2017.txt file and use 50States.txt to convert state names to their abbreivated form and store it in countyDemPrev
countyDemPrev: 50States.txt County_Prevalence_2017.txt
	python3 ./countyPrev.py > countyDemPrev

# find the total drug days per population over 65 per Dementia cases in each county by dividing ratio of drug days per population over 65 (from drugsPopCountyRatio) by prevalence of dementia (from countyDemPrev) and store in finalRatio
finalRatio: drugsPopCountyRatio countyDemPrev
	python3 ./drug_dem_county_ratio.py > finalRatio

#find the average income of each county using IncomePop.gz which has the average income per zip code and using the zipCountyConversion to convert those zip codes and their average income to counties - this results in the average incomes for those counties associated with Dementa drugs and store in countyIncome 
countyIncome: IncomePop.gz zipCountyConversion
	python3 ./incomeZip_to_county.py > countyIncome

# use finalRatio which has the drugs days divided by disease cases, the y axis, and use countyIncome which has average income per county, x axis, and store together in XandY
XandY: finalRatio countyIncome
	python3 ./countyXandY.py > XandY

# create the plot using XandY which has the x and y axis points 
plot.pdf: XandY
	python3 ./plot.py
