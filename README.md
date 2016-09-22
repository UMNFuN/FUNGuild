
<h1>FUNGuild: Fungi + fUNctional + Guild</h1>

Online version:<br>
http://funguild.org<br>
Databases:<br>
http://stbates.org/funguild_db.php<br>
http://stbates.org/nemaguild_db.php<br>
Api:<br>
api url = http://www.stbates.org/guilds/services/api/<br>
api url + query.php?qField=NAME OF DESIRED FIELD&qText=QUERY TEXT"<br>
e.g., http://www.stbates.org/guilds/services/api/query.php?qField=taxon&qText=Tulostoma<br>
Citation:<br>
Nguyen NH, Song Z, Bates ST, Branco S, Tedersoo L, Menke J, Schilling JS, Kennedy PG. In Press. FUNGuild: An open annotation tool for parsing fungal community datasets by ecological guild. Fungal Ecology.<br> (http://cbs.umn.edu/sites/cbs.umn.edu/files/public/downloads/Nguyenetal2015b_1.pdf)

****

GENERAL NOTES

The Guilds bioinformatic tool is a two-component system that includes online community annotated databases and a python script that assigns functional information to operational taxonomic units (OTUs) obtained from next generation sequencing of environmental samples. The script is based on an original in-house python script referenced in Branco et al. 2013. PLoS One 8:1–10 (http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0078295). It searches taxonomic strings in the user’s OTU table against the online Guilds databases (fungi or nematodes) containing taxonomic keywords and functional metadata. The output is the original OTU table with functional metadata appended, and users also have options to output an assigned OTUs only table and/or a table containing only OTUs for which assignments could not be made.

To run the Guilds bioinformatic tool locally, a current version of Python (https://www.python.org/) must be installed on the user’s local machine before the Guilds script (https://raw.githubusercontent.com/UMNFuN/FUNGuild/master/Guilds_v1.0.py) can be used. The Guilds databases are accessed by the python script remotely and, therefore, they do not need to be loaded to the user’s local machine. However, the script must be able to access the internet to connect with the databases.

An online version of the Guilds bioinformatic tool, the 'assignment application', is also available here:

http://funguild.org

An example OTU table .txt file to demonstrate formatting can be found <a href='http://www.stbates.org/guilds/download_examples.php/?download_file=otu_table_example.txt' target = '_blank'><i>here</i></a>.


RUNNING THE SCRIPT LOCALLY FROM THE COMMAND LINE

- Make sure you local computer has Python 2 installed (see https://www.python.org/downloads/).

- Copy the Guilds python script (https://raw.githubusercontent.com/UMNFuN/FUNGuild/master/Guilds_v1.0.py), paste it into a text file, and save it with the .py extension (e.g., Guilds_v1.0.py) rather than .txt (make sure that the hide extension setting is not activated, as the file might then actually save as e.g., Guilds_v1.0.py.txt).

- Open a terminal to run the script via command line (e.g., /Applications/Utilities/ and click on 'Terminal' for mac OR for Windows use Start or Start Menu and search for 'command' or 'cmd' and then click on the 'Command Prompt' icon). Be sure to follow any conventions (e.g., directory path formatting) that are relevant to your particular operating system.

- Next, cd (change directory in the command line) into folder (directory) where you saved your .py file containing the Guilds script (mac note - you can drag the desired folder from the finder into the terminal to get the directory path rather than having to type it). For example on mac, type something like this ```cd /Users/username/Documents/python_scripts``` into the terminal.

- Determine the path to your properly formatted (see above) OTU table (e.g., /Users/username/Documents/project/otu_table_example.txt).

- Make sure that your computer is connected to the Internet, as the script will need to access the online database of taxonomic key words.

- Make a Python call on the script (remember you should have already used the change directory command to cd into the folder that contains the script) giving the proper OTU table path (the -otu argument), desired taxonomic database (the -db argument; either ‘fungi’ or ‘nematode’; the default ‘fungi’ will be used if you don’t signify the -db argument), and desired output (add the argument -m to also output an OTU table with just the OTUs for which functional assignments could be made and/or -u to output a table with only OTUs that could not be assigned; a table that includes both the assigned and unassigned OTUs is the default output). For example on a mac, you would type something like this ```python Guilds_v1.0.py -otu /Users/username/Documents/project/otu_table_example.txt -db fungi -m -u``` into the terminal.

- Hit the enter/return key on your computer, and allow a few seconds for the script to do its magic!


<a name="contributing">CONTRIBUTING GUILD INFORMATION TO THE FUNGUILD DATABASE</a>

Data pertaining to particular fungal or nematode taxa can be submitted to the Guilds databases (FUNGuild_db or NEMAGuild_db) by contacting the database curators (xerantheum@gmail.com or scott.thomas.bates@gmail.com), or via the online submission application (http://www.stbates.org/guilds/entry.php - for an upload .txt file formatting example, <a href='http://www.stbates.org/guilds/download_examples.php/?download_file=db_upload_example.txt' target = '_blank'><i>click here</i></a>). All submitted entries will be reviewed by the database curators prior to being migrated to the main Guilds databases. Taxon entries proposed for addition to the databases will be accessable once they have been reviewed by the database curators and migrated to the main database. Once migrated, proposed entries will automatically be available to all using the Guilds bioinformatic tool to make annotated assignments to their OTU tables containing fungal or nematode taxa.

<b>Information should be entered into each Guilds database field, in sequence, as follows:</b>

- Taxon: The scientific name (e.g., Ganoderma).

- Taxon Level: A numeral corresponding the correct taxonomic level for the taxon (0 = keyword, 3 = Phylum, 4 = Subphylum, 5 = Class, 6 = Subclass, 7 = Order, 8 = Suborder, 9 = Family, 10 = Subfamily, 11 = Tribe, 12 = Subtribe, 13 = Genus, 15 = Subgenus, 16 = Section, 17 = Subsection, 18 = Series , 19 = Subseries, 20 = Species, 21 = Subspecies, 22 = Variety, 23 = Subvariety, 24 = Form, 25 = Subform, 26 = Form Species).

- Trophic Mode: One of three trophic categories [pathotroph = receiving nutrients at the expense of the host cells and causing disease (e.g., biotroph, parasite, pathogen, etc.); saprotroph = receiving nutrients by breaking down dead host cells (e.g., wood rotters, litter rotters, etc.); symbiotroph = receiving nutrients by exchanging resources with host cells (e.g., ectomycorrhiza, lichens, etc.)]. The concepts presented here are similar to those of Tedersoo et al. 2014. Global diversity and geography of soil fungi. Science 346(6213). DOI: 10.1126/science.1256688 (http://www.sciencemag.org/content/346/6213/1256688).

- Guild: Provide a relevant guild descriptor (e.g., "Algal Parasite", "Animal Gut Fungus", "Animal Pathogen", "Arbuscular Mycorrhizal", "Dark Septate Endophyte", "Dung Saprotroph", "Ectomycorrhizal", "Endophyte", "Foliar Endophyte", "Ericoid Mycorrhizal", "Litter Saprotroph", "Lichenicolous", "Lichenized", "Musicolous", "Mycoparasite", "Plant Pathogen", "Soil Saprotroph", "Undefined Saprotroph", "Wood Saprotroph", etc.). New guilds can be erected if necessary.

- Confidence Ranking: "Highly Probable" (= absolutely certain), "Probable" (= fairly certain), "Possible" (= suspected but not proven, conflicting reports given, etc.).

- Growth Form: A basic morphological category such as "Agaricoid", "Boletoid", "Clavarioid", "Cup Fungus", "Facultative Yeast", "Gasteroid", "Hydnoid", " Jelly Fungus", "Phalloid", "Polyporoid", "Pyrenomycete", "Resupinate", "Rust", "Secotioid", "Smut", "Yeast", or "Thallus" should be noted.

- Trait: Other functional or morphological traits such as "Brown Rot", "Hypogeous", "Poisonous", "White Rot" or "Contact Exploration Type" would be appropriate for this field.

- Notes: Any other relevant information related to the taxon (e.g., "Facultative human pathogen causing coccidioidomycosis" for Coccidioides immitis, "Host - Arecaceae - Casuarinaceae, Palmae, Sapotaceae" for Xylaria obovata, or "Syn. Umbilicaria" for Actinogyra).

- Citation/Source: Publication, website, etc. from which the corresponding guild information was derived. Data for taxa that is based on peer-reviewed publications is preferred. Formatting examples follow...
    
    Costa IPMW et al. 2012. Checklist of endophytic fungi from tropical regions. Mycotaxon 119:26

    Esslinger TL. 2014. North Dakota State University (http://www.ndsu.edu/pubweb/~esslinge/chcklst/chcklst7.htm)
    
    James TY et al. 2006. Nature 443:818-822
    
    Kurtzman CP, Fell JW, Boekhout T eds. 2011. The Yeasts, a Taxonomic Study. Fifth Edition. Vols 1-3. Elsevier, San Diego
    
    Tedersoo L, May TW, Smith ME. 2010. Mycorrhiza 20:217-263
    
    Outline of Ascomycota (http://www.fieldmuseum.org/myconet)
    
    http://www.apsnet.org/publications/commonnames/Pages/default.aspx



<a name="troubleshooting">TROUBLESHOOTING</a>

<b>Formatting:</b> The python script expects a standard OTU table as input (<i><a href="http://biom-format.org/documentation/biom_conversion.html" target="_blank">click here</a></i> for converting a biom file to an otu_table.txt file in qiime), and it is critical that this is formatted correctly before running the script. A typical OTU table in the text file format will look something like this:

OTU_ID(tab)sample1(tab)sample2(tab)sample3(tab)taxonomy(return)
OTU_10(tab)10002(tab)10004(tab)0(tab)Fungi;Basidiomycota;Agaricales;Cortinariaceae;Cortinarius(return)
OTU_20(tab)10003(tab)0(tab)10001(tab)Fungi;Ascomycota;Chaetothyriales;Herpotrichiellaceae;Cladophialophora

For a formatting example .txt file and a more complete OTU table representation <a href='http://www.stbates.org/guilds/download_examples.php/?download_file=otu_table_example.txt' target = '_blank'><i>click here</i></a>.

Common errors include the following (move down through this list as needed, more critical errors are at the top of the list):

- <b>The 'taxonomy' header</b>. The script looks for the word 'taxonomy' in the 'column header' row so that it knows which column the taxonomic strings can be found in (the script then searches strings in this column for taxonomic key words e.g., a particular genus name like 'Cortinarius'). The script will return an error if it can't find the taxonomy header in the first row. The word 'taxonomy', therefore, must be inserted at the top of the column (the header) containing taxonomic strings before the script will work.

- <b>An extra row at the top of the OTU table</b>. Programs, such as QIIME, for analyzing datasets generated in high-throughput sequencing (HTS) runs often use the Biological Observation Matrix (BIOM) format to reduce the density (i.e., lots of zeros) of the data matrix. With such programs, a note indicating that the file was converted to the standard format (see above) from the BIOM format is often inserted into the first row of the table. This extra row needs to be removed before running the script on the OTU table file (i.e., the first 'column header' row in the table should read 'OTU_ID(tab)sample1(tab)sample2...').

- <b>Use of the number sign</b>. In a similar manner to the above problem, programs for HTS analysis may also insert a number sign (#) in front of OTU identifier ('#OTU_ID') column heading. It is best to remove this number sign before running the script as it may interfere with OTU table loading.

- <b>Hidden characters</b>. If you open your OTU table file in a text editor, key characters like 'tab' and 'return' are encoded (as e.g., \t and \r or \n) and are typically hidden characters (they may also show up as odd symbols if you unhide them in your editor view). These hidden characters can cause all sorts of seemingly mysterious problems to occur for programs (just search http://stackoverflow.com/ for 'carriage return \r' to get an idea). The script was written to be as flexible as possible with these sort of encoding issues, but errors may still arise. One quick fix is to open the OTU table in Microsoft Excel, check to see that all the rows and column are lining up properly, and then re-save the OTU table as a 'Tab Delimited Text' (.txt) or 'Comma Separated Values' (.csv) file.

- <b>Quoted characters</b>. Programs (e.g., Microsoft Excel) that create 'Tab Delimited Text' and 'Comma Separated Values' (.csv) files typically use quotation marks to 'protect' certain characters (e.g, commas) when used in text (e.g., ...Oligochaeta;Stylaria;Stylaria_sp._aguinaldo,_1997) as they have the potential to be misread (e.g., causing a column split in a .csv file between 'aguinaldo' and '_1997'). To correct this issue, make sure that taxa in the taxonomic strings are separated with a semicolon (e.g., ...Ustilaginomycotina;Ustilago;Ustilago_maydis) rather than a comma and remove all commas from the text portion of the string (e.g., ...Oligochaeta;Stylaria;Stylaria_sp._aguinaldo_1997). After you have made this correction, you may also need to clear any quotation marks from your OTU table. Do this by opening the file in a text editor and then delete all the quotation marks (i.e., use the find/replace function to replace all quotes '"' with a blank '' - as in nothing, not a space - see note below).

- <b>Extra spaces</b>. Spaces can cause problems when a file is being read into a program, this is why they are typically replaced with an underscore in the taxonomic strings (e.g., 'Stylaria_sp.' in the above example). To correct this issue, open the OTU table in a text editor and remove space gaps (i.e., gaps that consist of more than a single space), and then clear all of the spaces (i.e., use the find/replace function to replace all spaces ' ' with an underscore '_').

<b>Online version of the script:</b> The online Guilds_v1.0.py application (http://www.stbates.org/guilds/app.php) calls the python code from php when the 'Begin Analysis' button is 'pushed'. This application should work well for properly formatted (see above) OTU tables of a smaller file size (e.g., less than 25MB). There is a well known issue with php page time outs for processes that take a long time (read: more than the php default of 30 seconds). The script runs quickly, typically just a few seconds, but server handling of large files (e.g., loading them through your browser) can take time. To allow time for script processes to complete, the php 'max_execution_time' has been set to 0 (i.e., no time limit). Even though removing this restriction should allow time for processes to complete, large files can cause other problems that will trip a 500 'Internal Server Error' flag.

When working with large OTU table files, consider the following:

- Zip OTU tables of a larger file size (e.g., over 10MB) before loading them onto the server. This approach has been tested with larger files and seems to be in working order; however, processing time is slowed considerably (which shouldn't be an issue for php page time outs - see above). You can always try larger OTU table sizes (up to 50MB when zipped), but a great deal of patience may be required. This being said, it is recommended that you use a local version of the program run from the command line to run the script (see below).

- Run the script locally. Running the script from your local computer via command line (see above) will eliminate server related issues, remove the need to zip the file, and should speed up processing times (files of 25MB or more will typically run in several seconds).
