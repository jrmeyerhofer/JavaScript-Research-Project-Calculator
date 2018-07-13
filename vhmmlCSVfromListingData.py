import csv
import json
import sys

###############################################################################
#
# This file takes in a Manuscript vhmml JSON file with just listing data
# and outputs a CSV file (id, country, city, repository, shelf mark,
# project number, permalink
#
###############################################################################

# Load JSON data file into a Python variable.
if len(sys.argv) > 1:
    filetoOpen = sys.argv[1]
else:
    filetoOpen = raw_input("Name of the vHMML JSON listing data file? ")

input = open(filetoOpen)

# load the JSON file data into a python object
data = json.load(input)
# close the open JSON file. just in case
input.close()

# TESTING: Print out all the JSON data
# print data

# delete file if exists? Don't need to, will just overwrite existing file
csvFile = 'csvfile_'+filetoOpen+'.csv'
f = open(csvFile, 'w')

# make the header string first, include all the fields so that no matter what
# they show up.
csvHeaderString = "id,"
csvHeaderString = csvHeaderString + "country,"
csvHeaderString = csvHeaderString + "city,"
csvHeaderString = csvHeaderString + "repository,"
csvHeaderString = csvHeaderString + "shelfmark,"
csvHeaderString = csvHeaderString + "hmmlProjectNumber,"
csvHeaderString = csvHeaderString + "permalink"

# TESTING
# print csvHeaderString

# write out the header row for the CSV file
csvHeaderString = csvHeaderString + "\n"
f.write(csvHeaderString)

# This for loop traverses the JSON file, and puts the value,
# if there, into a string
for x in data:
    if x["id"]:
        csvValuesString = str(x["id"]) + ','
    else:
        csvValuesString = csvValuesString + 'null,'
    if "country" in x:
        csvValuesString = csvValuesString + x["country"].encode('utf-8') + ','
    else:
        csvValuesString = csvValuesString + 'null,'
    if x["city"]:
        csvValuesString = csvValuesString + x["city"].encode('utf-8') + ','
    else:
        csvValuesString = csvValuesString + 'null,'
    if x["repository"]:
        csvValuesString = csvValuesString + x["repository"].encode('utf-8')+','
    else:
        csvValuesString = csvValuesString + 'null,'
    if "shelfmark" in x:
        csvValuesString = csvValuesString + x["shelfmark"].encode('utf-8')+','
    else:
        csvValuesString = csvValuesString + 'null,'
    if x["hmmlProjectNumber"]:
        csvValuesString = csvValuesString + str(x["hmmlProjectNumber"])+','
    else:
        csvValuesString = csvValuesString + 'null,'
    if x["permalink"]:
        csvValuesString = csvValuesString + str(x["permalink"])
    else:
        csvValuesString = csvValuesString + 'null'

    # TESTING
    # print csvValuesString

    csvValuesString = csvValuesString + '\n'
    f.write(csvValuesString)


# Python will convert \n to os.linesep. Close the file
f.close()

# Tell them we're done
print "Done! Open " + csvFile + " to view your CSV listing data."
