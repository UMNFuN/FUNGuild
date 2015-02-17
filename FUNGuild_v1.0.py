# -*- coding: utf-8 -*-
'''
This script assigns functional information to the OTUs in the user's OTU table. The OTU table need to have a column names 'taxonomy', containing information from a reference database (such as UNITE). It is required that the first line of the OTU table to be the header, without any additional comments. Some program, such as single_rarefaction.py in Qiime will add an additioal comment before the header, this has to be removed before using the FunGuild script. The script will try to recognized the delimiter in the user's OTU table, but comma (.csv) or tab delimiter format are recommended.

The functional database is fetched from Github (https://raw.githubusercontent.com/xerantheum/fungal_function/master/fungal_guild_table.txt)

Script usage: FunGuild.py [-h] [-otu OTU_file] [-m] [-u]

optional arguments:
  -h, --help       show this help message and exit
  -otu OTU         Path and file name of the OTU table. The script will try to
                   detect the delimiters in the file, but tab or csv are
                   preferred formats.
  -m, --matched    Ask the script to output a otu table with function assigned
                   OTUs
  -u, --unmatched  Ask the script to output a otu table with unassigned OTUs
  
This is an example command to run this script:
python FunGuild.py -otu user_otu_table.txt

The script will have one output file with suffix on the input file: user_otu_table.function.txt

By using -m and -u, the script will produce two additional files:
-m will output a file contains only the OTUs that has been assigned a function: user_otu_table.matched.txt
-u will output a file contains only the OTUs that do not have match in the database: user_otu_table.unmatched.txt

All existed files will be overwrote without notice.

All output OTU tables are sorted by the sum sequence number of each OTU.

###################################################################################
Development history:

The idea of parsing OTUs into functions originated from an python script by Sara Branco that separates EM, potentially EM and non-EM OTUs (Branco et al. 2013. PLoS One 8: 1–10).

The algorithm used by FunGuild was first developed by Scott Bates in R to assign functions to all fungi.

Current FunGuild script is developed by Zewei Song in python to improve performance and compatibility.
###################################################################################

Zewei Song
2/14/2015
songzewei@outlook.com
'''

#Import modules#################
import argparse
import os
import timeit
import sys
import urllib
from operator import itemgetter
import csv

start = timeit.default_timer()
################################

#Command line parameters#####################################################################
parser = argparse.ArgumentParser()

parser.add_argument("-otu", help="Path and file name of the OTU table. The script will try to detect the delimiter"
					"in the file, but tab or csv are preferred formats.") 
parser.add_argument("-m", "--matched", action="store_true", help="Ask the script to output a otu table with function assigned OTUs") 
parser.add_argument("-u", "--unmatched", action="store_true", help="Ask the script to output a otu table with function assigned OTUs")

args = parser.parse_args()

#input files
otu_file = args.otu

#Detect delimiter in the input file
with open(otu_file, 'r') as f1:
    dialect = csv.Sniffer().sniff(f1.read())
    f1.seek(0)
    otu_delimiter = dialect.delimiter

#output files
dot_position = [i for i in range(len(otu_file)) if otu_file.startswith('.', i)] #Get the position of . in the input filename

if not dot_position: #the file does not have extension
	matched_file = args.otu + '.matched.txt'
	unnmatched_file = args.otu + '.unmatched.txt'
	total_file = args.otu + '.function.txt'
else:
	matched_file = args.otu[:dot_position[-1]] + '.matched.txt'
	unmatched_file = args.otu[:dot_position[-1]] + '.unmatched.txt'
	total_file = args.otu[:dot_position[-1]] + '.function.txt'
###########################################################################################

# Import Function Database from GitHub, and get it ready.##################################
print "FUNGuild v1.0 Beta"
print "Downloading database from Github ..."

function_file = 'temp_db.txt' #temp file to store database file
url = "https://raw.githubusercontent.com/UMNFuN/FUNGuild/master/FUNGuild_DB.txt"

urllib.urlretrieve(url, function_file) # Save the online database to a local temp file.

#Sometimes Github file has \r instead of \n at the end of each line. This arises problem in Windows platform.
#Replace all \r with \n.
f_database = open(function_file, 'r')
new_line = []
for line in f_database:
	new_line.append(line.replace('\r','\n'))

f_database.close()

output = open(function_file,'w')
for item in new_line:
	output.write('%s' %item)
output.close()

#Detect the position of header
f_database = open(function_file, 'r') # Open the database file.
for line in f_database:
	if line.find('Taxon') != -1: #Search for the line that contains the header (if it is not the first line)
		header_database = line.split('\t')
		break
f_database.close()

#Check the database header.
if len(header_database) == 1:
	header_database = header_database[0].split(" ")

header_database = header_database[2:] #Remove the 'Taxon' and 'Taxon level' columns.
# Set the parameters for progress report
with open(function_file) as f1:
    i = 0    
    for line in f1:
        i += 1
total_length = float(i) #length of the database

p = range(1,11)
way_points = [int(total_length*(x/10.0)) for x in p]
############################################################################################		

# Open the OTU table and read in the header ################################################
print ""
print "Reading in the OTU table: '%s'" %(args.otu)
print ""

#load the header and detect the delimiter in the file
with open(otu_file) as otu:
	header = otu.next().rstrip('\n').split(otu_delimiter) 

if 'taxonomy' not in header: #Check if 'taxonomy' is an individual item in the header list.
	taxonomy_checker = "".join(header)
	if taxonomy_checker.find('taxonomy') != -1:  #Check if 'taxonomy' is attached with other column names.
		print 'Taxonomy column is present but the header of your OTU table is not properly formated. Please check the help document for the format of the OTU table.'
	else:
		print 'Cannot find the taxonomy column, please check you OTU table.'
	sys.exit(0)

#Attach all columns of database file to the header of the new OTU table
for item in header_database:
	header.append(item)

# get the positions of the taxonomy column and Notes column
index_tax = header.index('taxonomy')
index_notes = header.index('Notes')

#Abort if the column 'taxonomy' is not found
if index_tax == -1:
	print "Column 'taxonomy' not found. Please check you OTU table %s." %(otu_file)
	sys.exit(0)
############################################################################################

#Search in function database################################################################
# Read the OTU table into memory, and separate taxonomic levels with '@'.
with open(otu_file) as otu:
	otu_tab = []    
	for record in otu:
		otu_current = record.split(otu_delimiter)
		otu_taxonomy = otu_current[index_tax].rstrip('\n')
		replace_list = ['_',' ',';',',']
		for symbol in replace_list:
			otu_taxonomy = otu_taxonomy.replace(symbol, '@')
		otu_taxonomy = otu_taxonomy + '@'
		otu_current[index_tax] = otu_taxonomy
		otu_tab.append(otu_current)
	otu_tab = otu_tab[1:] # remove the header line

# Start searching the database
## Each record in the Fungal Guild Database is searched in the user's OTU table.
count = 0 # count of matching records in the OTU table
percent = 0 # line number in the database

otu_redundant = []
otu_new = []

print "Searching the function database..."

f_database = open(function_file, 'r')
for record in f_database:
    # report the progress   
    percent += 1
 
    if percent in way_points:
        progress = (int(round(percent/total_length*100.0)))
        print '{}%'.format(progress) 
    else: t = 0
    
    # Compare database with the OTU table
    function_tax = record.split('\t')
    search_term = function_tax[0].replace(' ', '@') #first column of database, contains the name of the species
    search_term = '@' + search_term + '@' #Add @ to the search term

    for otu in otu_tab:
        otu_tax = otu[index_tax] # Get the taxonomy string of current OTU record.
        if otu_tax.find(search_term) >= 0: #found the keyword in this OTU's taxonomy
            count += 1 # Count the matching record
            otu_new = otu[:]
            
            # Assign the matching functional information to current OTU record.
            for item in function_tax:
                otu_new.append(item)
            otu_redundant.append(otu_new)
f_database.close()

# Finish searching, delete the temp function database file
if os.path.isfile('temp_db.txt') == True: 
	os.remove('temp_db.txt')        

print ""
print "Found %i matching taxonomy records in the database."%(count)
print "Dereplicating and sorting the result..."

#Dereplicate and write to output file##########################################################
#Sort by OTU names and Level. Level is sorted from species to kingdom.
otu_sort = otu_redundant[:]
otu_sort.sort(key = itemgetter(index_tax), reverse = True) # Sort the redundant OTU table by Taxonomic Level.
otu_sort.sort(key = itemgetter(0)) # Sort the redundant OTU table by OTU ID.

#Dereplicate the OTU table, unique OTU ID with lowest taxonomic level will be kept.
otu_id_list = []
unique_list = []
count = 0

for item in otu_sort:
    if item[0] not in otu_id_list:
        count += 1
        otu_id_list.append(item[0])
        unique_list.append(item)

#Copy the original taxonomy string (without @) to the unique OTU table
otu_tax = []
with open(otu_file) as f_otu:
    for otu in f_otu:
        temp = otu.rstrip('\n').split(otu_delimiter)        
        otu_tax.append(temp)
    otu_tax = otu_tax[1:]
    
for new_rec in unique_list:
    for rec in otu_tax:
        if new_rec[0] == rec[0]:
            new_rec[index_tax] = rec[index_tax]
#Sort the new otu table by the total sequence number of each OTU.
unique_list.sort(key=lambda x: int(sum(map(int,x[1:index_tax]))), reverse=True)
################################################################################################

#Write to output files##############################################################################
#Output matched OTUs to a new file
if args.matched:
	if os.path.isfile(matched_file) == True:
		os.remove(matched_file)
	output = open(matched_file,'a')
	#Write the matched list header
	output.write('%s' % ('\t'.join(header))) #Header

	#Write the matched OTU table
	for item in unique_list:
		rec = '\t'.join(item)    
		output.write('%s' % rec)
	output.close()

#Output unmatched OTUs to a new file
unmatched_list = []    

for rec in otu_tax:
	count2 = 0        
	for new_rec in unique_list:
		if rec[0] == new_rec[0]: #Check if the current record is in the unique_list (has been assigned a function)
			count2 += 1
	if count2 == 0:
		unmatched_list.append(rec)

count_unmatched = 0

#Add 'Unassigned' to the 'Notes' column
for item in unmatched_list:
	l = len(header) - len(item)
	for i in range(l):
		item.extend('-')
	item[index_notes] = 'Unassigned'

if args.unmatched:
	if os.path.isfile(unmatched_file) == True: 
		os.remove(unmatched_file)
	output_unmatched = open(unmatched_file, 'a')
	output_unmatched.write('%s' % ('\t'.join(header)))		
	for item in unmatched_list:
		rec = '\t'.join(item)
		output_unmatched.write('%s\n' % rec)
		count_unmatched += 1
	output_unmatched.close()
 
#Output the combined matched and unmatched OTUs to a new file
if os.path.isfile(total_file) == True: 
	os.remove(total_file)

total_list = unique_list + unmatched_list #Combine the two OTU tables
total_list.sort(key=lambda x: int(sum(map(int,x[1:index_tax]))), reverse=True) #Sorted the combined OTU table

output_total = open(total_file, 'a')
output_total.write('%s' % ('\t'.join(header)))

count_total = 0
for item in total_list:
	rec = ('\t'.join(item)).strip('\n')
	output_total.write('%s\n' % rec)
	count_total += 1
output_total.close()
####################################################################################################################

#Print report on the screen#########################################################################################
print "FunGuild tried to assign function to %i OTUs in '%s'."  %(count_total, otu_file)
print "%i OTUs were assigned a function." %(count)
print "Result saved to '%s'" %(total_file)

if args.matched or args.unmatched:
	print '\nAdditional output:'
	if args.matched:
		print "%i OTUs have been assigned functions and saved to %s." %(count, matched_file)
	if args.unmatched:
		print "%i OTUs were not assigned for a function, these are saved to %s." %(count_unmatched, unmatched_file)

# Finish the program
stop = timeit.default_timer()
runtime = round((stop-start),2)
print "\nTotal calculating time: {} seconds.".format(runtime)
####################################################################################################################