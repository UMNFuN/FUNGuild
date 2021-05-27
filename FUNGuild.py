#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 10:36:47 2018

Coders who love to comment their code are unlikely to have bad luck.

@author: Zewei Song
@email: songzewei@genomics.cn
"""
#%
from __future__ import print_function
from __future__ import division
import argparse
import textwrap
import sys
import pandas as pd
import json
from urllib.request import urlopen

parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter, \
                                     description=textwrap.dedent('''\
                                    FUNGuild v1.2 for parsing fungal functional information from taxonomic data.
                                    
                                    It takes two steps (parsers) to query the database of FUNGuild:
                                        
                                    The first step/parser takes in an user provided OTU table, and extract
                                    its taxonomic strings for all OTUs. The taxonomic strings are then parsed
                                    and divided into the seven major levels (k, p, c, o, f, g, s). The result
                                    is saved in a new file with .taxa suffix.
                                    
                                    The second step/parser takes in the taxa output, and search all keywords
                                    in FUNGuild. One the match at the lowest level will be reported (i.e. s > g > f).
                                    The output file will have a .guild suffix.
                                    
                                    The taxa parse insures that we have the right format of taxonomy for
                                    querying the database, thus significantly reducing unnecessary errors.
                                    The users can also compile a taxa parser output as the input for the 
                                    guild parser.
                                                                 '''),
                                     epilog=textwrap.dedent('''\
                                    ------------------------
                                    EXAMPLE:
                                    Assume we have an OTU table saved as tab-delimited format,
                                    with the last column as taxonomy from sintax.
                                        FUNGuild.py taxa -otu otu_table.txt -format tsv -classifier sintax
                                        FUNGuild.py guild -taxa otu_table.taxa.txt
                                    The final output will save in otu_table.taxa.guilds.txt
                                    Citation: FUNGuild: An open annotation tool for parsing fungal community
                                              datasets by ecological guild, Nguyen et al (2016) Fungal Ecology 20:241-248
                                    License: Creative Commons Licence
                                    Bug-reports and requests at: https://github.com/UMNFuN/FUNGuild
                                    ------------------------'''), prog='FUNGuild', usage='%(prog)s.py <parser: taxa|guild> <arguments>')
# parser = argparse.ArgumentParser(prog='FUNGuild.py')
parser.add_argument('action', choices=['taxa', 'guild'], metavar='taxa|guild', help=argparse.SUPPRESS)
taxa_parser_group = parser.add_argument_group('Arguments for taxa parser', 'Step1: parse an OTU table for the taxonomic keywords.')
taxa_parser_group.add_argument('-otu', default='otu_table.txt', help='User provided OTU table.')
taxa_parser_group.add_argument('-format', default='tsv', choices=['tsv', 'csv', 'biom-json'], help='Table format chose from tsv, csv, or biom-json. Default: tsv')
taxa_parser_group.add_argument('-column', default='taxonomy', help='Value of the taxonomic column in the OTU table. Default: taxonomy')
taxa_parser_group.add_argument('-classifier', default='unite', choices=['unite', 'sintax'], help='The type of taxonomic string. Default: unite')
guild_parser_group = parser.add_argument_group('Arguments for guild parser', 'Step2: search the extracted taxonomy against FUNGuild.')
guild_parser_group.add_argument('-taxa', default='otu_table.taxa.txt', help='The output from taxa parser.')
args = parser.parse_args()

def taxa_parser(otu, fmt, column, classifier):
    input_otu = otu
    otu_format = fmt
    taxa_column = column
    taxa_format = classifier
    if otu_format in ['tsv', 'csv']:
        output_taxa = otu.split('.')
        output_taxa = output_taxa[:-1] + ['taxa'] + [output_taxa[-1]]
        output_taxa = '.'.join(output_taxa)
    elif otu_format == 'biom-json':
        output_taxa = otu.split('.')
        output_taxa = output_taxa[:-1] + ['taxa'] + ['txt']
        output_taxa = '.'.join(output_taxa)        

    # Read in the OTU table and extract the taxonomic column.
    # All taxonomy are converted to Pandas DataFrame.
    # print('Reading in {0} ...'.format(input_otu))
    if otu_format == 'tsv':
        otu = pd.read_csv(input_otu, sep='\t', header=0, index_col=0, comment='#')
        otu_id = list(otu.index)
        taxa = list(otu[taxa_column]) # Save the taxa information
        taxa = pd.DataFrame(taxa, index=otu_id, columns=[taxa_column])
    elif otu_format == 'csv':
        otu = pd.read_csv(input_otu, sep=',', header=0, index_col=0, comment='#')
        otu_id = list(otu.index)
        taxa = list(otu[taxa_column])
        taxa = pd.DataFrame(taxa, index=otu_id, columns=[taxa_column])
    elif otu_format == 'biom-json':
        otu = json.loads(open(input_otu).read())
        taxa_lines = []
        otu_id = []
        for line in otu['rows']:
            taxa_lines.append(line['metadata'][taxa_column])
            otu_id.append(line['id'])
        taxa = pd.DataFrame(taxa_lines, index=otu_id, columns=[taxa_column])
    else:
        print('Please enter the right OTU table format.')
        sys.exit()

    # Parse the taxonomy column into separated taxa levels
    taxa_level = []
    taxa_otu = []
    taxa_dict = {}
    
    level = ['k', 'p', 'c', 'o', 'f', 'g', 's']
    for record in taxa.iterrows():
        current_otu = record[0]
        if taxa_format == 'unite':
            taxa_string = record[1][taxa_column].split('|')
            if len(taxa_string) == 6: # The string has the UNITE label
               taxa_string = taxa_string[5].split(';')
            elif len(taxa_string) == 1:
                taxa_string = taxa_string[0].split(';')
            taxa_string = [i[3:] for i in taxa_string] # Remove the k__, f__, g__ prefix
        elif taxa_format == 'sintax':
            taxa_string = record[1][taxa_column].split(',')
            taxa_string = [i[2:] for i in taxa_string] # Remove the d:, f:, g: prefix
            taxa_string = [i.split('(')[0] for i in taxa_string] # Remove confidnet value
        else:
            pass
        if len(taxa_string) < 7: # check if there are missing taxonomic levels
            taxa_string = taxa_string + ['na'] * (7 - len(taxa_string))
        taxa_otu.append(current_otu)
        taxa_level.append(taxa_string)
        taxa_dict[record[0]] = {}
        for l, v in zip(level, taxa_string):
            taxa_dict[record[0]][l] = v

    # Output to file
    otu_id = list(taxa.index)
    output = [['OTU_ID'] + ['Kingdom', 'Phylum', 'Class', 'Order', 'Family', 'Genus', 'Species']]
    for otu in otu_id:
        current_line = [otu]
        for item in level:
            current_line.append(taxa_dict[otu][item])
        output.append(current_line)
    with open(output_taxa, 'w') as f:
        for line in output:
            f.write('%s\n' % '\t'.join(line))
    print('Parsed taxa file: {0}'.format(output_taxa))        

def guild_parser(taxa):
    taxa_input = taxa
    url = 'https://mycoportal.org/fdex/services/api/db_return.php?dbReturn=Yes'
    # Output file name
    dot_position = [i for i in range(len(taxa_input)) if taxa_input.startswith('.', i)] #Get the position of . in the input filename
    if not dot_position: #the file does not have extension
    	output_file = taxa_input + '.guilds.txt'
    else:
    	output_file = taxa_input[:dot_position[-1]] + '.guilds.txt'

    # Import database
    print('Connecting with FUNGuild database ...')
    db_content = json.load(urlopen(url + '&pp=1'))
    db = []
    for current_record in db_content:
        #current_record = json.loads(record)
        if current_record['taxonomicLevel'] == 20: # If species level
            current_record['taxon'] = current_record['taxon'].replace(' ', '_')
        db.append(current_record)
    print('Found {0} records in the db.'.format(len(db)))
    
    # Build searching dictionary
    search_dict = {}
    for item in db:
        search_dict[item['taxon']] = item

    # Read in otuput from the taxa parser
    taxa_parser_input = taxa_input
    level = ['k', 'p', 'o', 'c', 'f', 'g', 's']
    output_columns = ['taxon', 'taxonomicLevel', 'trophicMode', 'guild', 'trait', 'growthForm', 'confidenceRanking', 'notes', 'citationSource']
    
    taxa = []
    with open(taxa_parser_input, 'r') as f:
        for line in f:
            taxa.append(line.strip('\n').split('\t'))
        taxa = taxa[1:] # Read in all data except the header

    # Search all taxa terms for functions in FUNGuild
    print('Search initiated.')
    taxa_function = []
    for record in taxa:
        current_record = [record[0]]
        checker = 0
        for level in record[::-1][:-1]: # Start search from the lowest (species) level
            if checker == 1:
                break
            else:
                try:
                    current_function = search_dict[level] # If current level is in the database
                    for item in output_columns:
                        current_record.append(current_function[item])
                    checker = 1 # Stop at the lowest matching level
                except KeyError:
                    pass
        if len(current_record) == 1: # if no matching record
            for item in output_columns:
                current_record.append('na')
        else:
            pass
        taxa_function.append(current_record)
    print('Search finished.')
    # Write the results to a file
    header = ['OTU', 'Kingdom', 'Phylum', 'Order', 'Class', 'Family', 'Genus', 'Species'] + output_columns
    output = [header]
    for taxonomy, function in zip(taxa, taxa_function):
        current_line = taxonomy + function[1:]
        output.append(current_line)
    
    with open(output_file, 'w') as f:
        for line in output:
            f.write('%s\n' % '\t'.join([str(i) for i in line]))
    print('FUNGuild results wrote to {0}.'.format(output_file))




if args.action == 'taxa':
    print('Taxa parser initiated.')
    otu = args.otu
    fmt = args.format
    column = args.column
    classifier = args.classifier
    print('Loading OTU table: {0}'.format(otu))
    print('Table format: {0}'.format(fmt))
    print('Taxonomic column: {0}'.format(column))
    print('Taxonomic style: {0}'.format(classifier))
    taxa_parser(otu, fmt, column, classifier)
elif args.action == 'guild':
    print('Guild parser initiated')
    taxa = args.taxa
    print('Loading taxa file: {0}'.format(taxa))
    guild_parser(taxa)
else:
    print('Unknown function, please check the manual using -h or --help.')

