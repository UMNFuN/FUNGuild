<h1>FUNGuild: Fungi + fUNctional + Guild</h1>

<h2>We continue to work behind the scenes to provide updates and support for the FUNGuild Database.
We expect to release the next version of the database in Spring 2024. Currently, the database includes over 13,000 fungal taxa!

<h3>Quick start</h3>

The FUNGuild.py script was written under Python 3 environment. If you don't have a Python 3 environment, install [Miniconda](https://docs.conda.io/projects/miniconda/en/latest/) or the more comprehensive [Anaconda](https://www.anaconda.com/download).

The current version of FUNGuild (Guilds_v1.1.py) parses guilds in two steps. First we implemented a taxa parser to extract taxonomic information from the user provided OTU table. Then we use a guild parser to query the FUNGuild database. In this way, we can avoid most of the format issues we encountered when dealing with the original OTU table. You can also compile your own taxa file (names only in rows) as the input for the guild parser.

Use -h or --help for a detail FUNGuild manual.

Preparing your workspace:
```
git clone https://github.com/UMNFuN/FUNGuild
cd FUNGuild/
```
Run the script using default parameters:
```
python Guilds_v1.0.py -otu /Users/username/Documents/project/otu_table.txt -db fungi
```
****
<b>Use the FUNGuild Online version to query the database:</b><br>
http://funguild.org<br>

<b>Databases:</b><br>
http://stbates.org/funguild_db.php<br>
http://stbates.org/nemaguild_db.php<br>

<b>API:</b><br>
api url = https://mycoportal.org/funguild/services/api/<br>
api url + db_return.php?qDB=NAME OF DESIRED DATABASE&qField=NAME OF DESIRED FIELD&qText=QUERY TEXT"<br>
e.g., https://mycoportal.org/funguild/services/api/db_return.php?qDB=funguild_db&qField=taxon&qText=Tulostoma<br>

<b>Citation:</b><br>
Nguyen NH, Song Z, Bates ST, Branco S, Tedersoo L, Menke J, Schilling JS, Kennedy PG. 2016. FUNGuild: An open annotation tool for parsing fungal community datasets by ecological guild. Fungal Ecology 20:241–248. [Download paper](https://cbs.umn.edu/sites/cbs.umn.edu/files/public/downloads/Nguyenetal2015b.pdf)

****

<b>Contributors:</b> Michelle Afkhami, Carlos Aguilar-Trigueros, Scott T. Bates, Sarah Branco, Posy Busby, Natalie Christian, Will Cornwell, Zachary Foster, Fukasawa Fu, Romina Gazis, Rannveig Jacobsen, Peter Kennedy, Daniel Lindner, Jon Menke, Amy Milo, Sara Moss, Nhu Nguyen, Henrik Nilsson, Jonathan Reich, Jonathan Schilling, Zewei Song, Jennifer Talbot, Leho Tedersoo, Nathaniel Tobey, Will VanHook, and Amy Zanne

****

<h3>IMPORTANT: Interpretation of data</h3>
We highly recommend that users of FUNGuild read through the <a href="https://github.com/UMNFuN/FUNGuild/blob/master/FUNGuild_Manual.pdf">manual</a> and the <a href="https://cbs.umn.edu/sites/cbs.umn.edu/files/public/downloads/Nguyenetal2015b.pdf">paper</a> for suggestions on interpretation of your guild data.

****
<h3>General notes</h3>

The Guilds bioinformatic tool is a two-component system that includes online community annotated databases and a python script that assigns functional information to operational taxonomic units (OTUs), including amplicon sequence variants (ASVs) obtained from sequencing of environmental samples. The script is based on an original in-house python script referenced in [Branco et al. 2013](http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0078295) and has matured over the years. It searches taxonomic strings in the user’s contingency table (OTU table) against the online Guilds databases (fungi or nematodes) containing taxonomic classification and functional metadata. The output is the original OTU table with functional metadata appended, and users also have options to output an OTU table with database matches only and/or a table containing only OTUs with no matches.

The current version only support running the tool locally. A current version of [Python](https://www.python.org/) must be installed on the user’s local machine before the [Guilds parser script](https://raw.githubusercontent.com/UMNFuN/FUNGuild/master/Guilds_v1.0.py) can be used. The Guilds databases are accessed by the python script remotely (internet required) and, therefore, they do not need to be loaded to the user’s local machine.

We also provide an [example OTU table](https://github.com/UMNFuN/FUNGuild/blob/master/example/otu_table.txt) to demonstrate general formatting.

***
<h3>Running the script locally from command line</h3>

- Make sure your local computer has Python installed. Our current version of script (Guilds_v1.0.py) supports Python version higher than 2.7. We recommend that you install the [Miniconda](https://docs.conda.io/projects/miniconda/en/latest/) or [Anaconda](https://anaconda.org/download) Python distribution for all required dependencies. Python 3.6 is prefered for its better support of Unicode characters.

- We use the Python package <i>requests</i> for connecting with the FUNGuild database. This package should come with most of the common Python distributions. If your Python distribution doesn't have this package (i.e. you get this error: ImportError: No module named requests), you can install it using: pip install requests

- Download or copy the [Guilds parser script](https://raw.githubusercontent.com/UMNFuN/FUNGuild/master/Guilds_v1.1.py). The script should be saved in a file with the .py extension (e.g., Guilds_v1.1.py) rather than .txt (make sure that the "hide extension" setting is not activated, as the file might then actually save as e.g., Guilds_v1.1.py.txt).

- Download the [example OTU table](https://github.com/UMNFuN/FUNGuild/blob/master/example/otu_table.txt) if you want to test out this script or have not used it before.
  
- Open a terminal via command line (e.g., /Applications/Utilities/ and click on 'Terminal' for Mac; for Windows use Start or Start Menu and search for 'command' or 'cmd' and then click on the 'Command Prompt' icon). Be sure to follow any conventions (e.g., directory path formatting) that are relevant to your particular operating system.
```
mkdir /Users/username/Documents/FUNGuild
git clone https://github.com/UMNFuN/FUNGuild/
```
- Next, cd (change directory in the command line) into folder (directory) where you saved your .py file containing the Guilds script (Mac users - you can drag the desired folder from the finder into the terminal to get the directory path rather than having to type it). For example on mac, type something like this into the terminal:
```
cd /Users/username/Documents/FUNGuild
```
- Determine the path to your properly formatted (see above) OTU table (e.g., /Users/username/Documents/project/otu_table_example.txt).

- Make sure that your computer is connected to the Internet, as the script will need to access the online database.

- Make a Python call on the script (remember you should have already used the change directory command to cd into the folder that contains the script) giving the proper OTU table path (the `-otu` argument), desired taxonomic database (the `-db` argument; either `fungi` or `nematode`; the default `fungi` will be used if you don’t input the -db argument), and desired output (add the argument `-m` to also output an OTU table with just the OTUs for which functional assignments could be made and/or `-u` to output a table with only OTUs that could not be assigned; a table that includes both the assigned and unassigned OTUs is the default output). For example on a mac, you would type something like this into the terminal:
```
python Guilds_v1.0.py -otu /Users/username/Documents/project/otu_table_example.txt -db fungi -m -u
```
- Hit the enter/return key on your computer, and allow a few seconds for the script to do its magic!

****

<h3><a name="contributing">CONTRIBUTING GUILD INFORMATION TO THE FUNGUILD DATABASE</a></h3>

Data pertaining to particular fungal or nematode taxa can be submitted to the Guilds databases (FUNGuild_db or NEMAGuild_db) by contacting the database curators (Nhu Nguyen <nhu.nguyen@hawaii.edu> or Scott Bates <scott.thomas.bates@gmail.com>). All submitted entries will be reviewed by the database curators prior to being migrated to the main Guilds databases. Taxon entries proposed for addition to the databases will be accessable once they have been reviewed by the database curators and migrated to the main database. Once migrated, proposed entries will automatically be available to all using the Guilds bioinformatic tool to make annotated assignments to their OTU tables containing fungal or nematode taxa.

<b>Information should be entered into each Guilds database field, in sequence, as follows:</b>

- Taxon: The scientific name (e.g., Ganoderma).

- Taxon Level: A numeral corresponding the correct taxonomic level for the taxon (0 = keyword, 3 = Phylum, 4 = Subphylum, 5 = Class, 6 = Subclass, 7 = Order, 8 = Suborder, 9 = Family, 10 = Subfamily, 11 = Tribe, 12 = Subtribe, 13 = Genus, 15 = Subgenus, 16 = Section, 17 = Subsection, 18 = Series , 19 = Subseries, 20 = Species, 21 = Subspecies, 22 = Variety, 23 = Subvariety, 24 = Form, 25 = Subform, 26 = Form Species).

- Trophic Mode: One of three trophic categories [Pathotroph = receiving nutrients at the expense of the host cells and causing disease (e.g., biotroph, parasite, pathogen, etc.); Saprotroph = receiving nutrients by breaking down dead host cells (e.g., wood rotters, litter rotters, etc.); Symbiotroph = receiving nutrients by exchanging resources with host cells (e.g., ectomycorrhiza, lichens, etc.)]. The concepts presented here are similar to those of [Tedersoo et al. 2014](http://www.sciencemag.org/content/346/6213/1256688).

- Guild: Provide a relevant guild descriptor [Pathotroph: Animal Pathogen (including human pathogens - typically annoated as such), Bryophyte Parasite, Clavicipitaceous Endophyte, Fungal Parasite, Lichen Parasite, Plant Pathogen; Saprotroph: Dung Saprotroph (i.e., coprophilous), Leaf Saprotroph (e.g., leaf litter decomposer), Plant Saprotroph, Soil Saprotroph (e.g., rhizosphere saprobe - typically annoated as a rhizosphere fungus), Undefined Saprotroph (e.g., a general saprobe, or in cases where the ecology is not known but suspected to be a saprobe), Wood Saprotroph (e.g., wood rotting fungi); Symbiotroph: Ectomycorrhizal, Ericoid Mycorrhizal, Endophyte, Epiphyte, Lichenized (i.e., lichen)]. New guilds can be erected if necessary.

- Confidence Ranking: "Highly Probable" (= absolutely certain), "Probable" (= fairly certain), "Possible" (= suspected but not proven, conflicting reports given, etc.).

- Growth Form: Basic morphological categories including "Agaricoid", "Boletoid", "Clathroid", "Clavarioid", "Corticioid", "Facultative Yeast", "Gasteroid", "Hydnoid", "Microfungus", "Phalloid", "Polyporoid", "Rust", "Secotioid", "Smut", "Thallus", "Tremelloid", or "Yeast" should be noted.

- Trait: Other functional or morphological traits such as "Brown Rot", "Hypogeous", "Poisonous", "Soft Rot", "White Rot" or "Contact Exploration Type" would be appropriate for this field.

- Notes: Any other relevant information related to the taxon (e.g., "Facultative human pathogen causing coccidioidomycosis" for Coccidioides immitis, "Host - Arecaceae - Casuarinaceae, Palmae, Sapotaceae" for Xylaria obovata, or "Syn. Umbilicaria" for Actinogyra).

- Citation/Source: Publication, website, etc. from which the corresponding guild information was derived. Data for taxa that is based on peer-reviewed publications is preferred. Formatting examples follow...
    
    Costa IPMW et al. 2012. Checklist of endophytic fungi from tropical regions. Mycotaxon 119:26

    Esslinger TL. 2014. North Dakota State University (http://www.ndsu.edu/pubweb/~esslinge/chcklst/chcklst7.htm)
    
    James TY et al. 2006. Nature 443:818-822
    
    Kurtzman CP, Fell JW, Boekhout T eds. 2011. The Yeasts, a Taxonomic Study. Fifth Edition. Vols 1-3. Elsevier, San Diego
    
    Tedersoo L, May TW, Smith ME. 2010. Mycorrhiza 20:217-263
    
    Outline of Ascomycota (https://www.fieldmuseum.org/sites/default/files/Myconet_13a.pdf)
    
    http://www.apsnet.org/publications/commonnames/Pages/default.aspx

****

<h3><a name="troubleshooting">TROUBLESHOOTING</a></h3>

<b>Formatting:</b> The python script expects a standard OTU table as input (<a href="http://biom-format.org/documentation/biom_conversion.html" target="_blank">click here</a> for converting a biom file to an otu_table.txt file in qiime), and it is critical that this is formatted correctly before running the script. A typical OTU table in the text file format will look something like this:

OTU_ID(tab)sample1(tab)sample2(tab)sample3(tab)taxonomy(return)
OTU_10(tab)10002(tab)10004(tab)0(tab)Fungi;Basidiomycota;Agaricales;Cortinariaceae;Cortinarius(return)
OTU_20(tab)10003(tab)0(tab)10001(tab)Fungi;Ascomycota;Chaetothyriales;Herpotrichiellaceae;Cladophialophora

We also provide an [example OTU table](https://github.com/UMNFuN/FUNGuild/blob/master/example/otu_table.txt) to demonstrate general formatting.

Common errors include the following (move down through this list as needed, more critical errors are at the top of the list):

- <b>The 'taxonomy' header</b>. The script looks for the word 'taxonomy' in the 'column header' row so that it knows which column the taxonomic strings can be found in (the script then searches strings in this column for taxonomic key words e.g., a particular genus name like 'Cortinarius'). The script will return an error if it can't find the taxonomy header in the first row. The word 'taxonomy', therefore, must be inserted at the top of the column (the header) containing taxonomic strings before the script will work.

- <b>An extra row at the top of the OTU table</b>. Programs, such as QIIME, for analyzing datasets generated in high-throughput sequencing (HTS) runs often use the Biological Observation Matrix (BIOM) format to reduce the density (i.e., lots of zeros) of the data matrix. With such programs, a note indicating that the file was converted to the standard format (see above) from the BIOM format is often inserted into the first row of the table. This extra row needs to be removed before running the script on the OTU table file (i.e., the first 'column header' row in the table should read 'OTU_ID(tab)sample1(tab)sample2...').

- <b>Use of the number sign</b>. In a similar manner to the above problem, programs for HTS analysis may also insert a number sign (#) in front of OTU identifier ('#OTU_ID') column heading. It is best to remove this number sign before running the script as it may interfere with OTU table loading.

- <b>Hidden characters</b>. If you open your OTU table file in a text editor, key characters like 'tab' and 'return' are encoded (as e.g., \t and \r or \n) and are typically hidden characters (they may also show up as odd symbols if you unhide them in your editor view). These hidden characters can cause all sorts of seemingly mysterious problems to occur for programs (just search http://stackoverflow.com/ for 'carriage return \r' to get an idea). The script was written to be as flexible as possible with these sort of encoding issues, but errors may still arise. One quick fix is to open the OTU table in Microsoft Excel, check to see that all the rows and column are lining up properly, and then re-save the OTU table as a 'Tab Delimited Text' (.txt) or 'Comma Separated Values' (.csv) file.

- <b>Quoted characters</b>. Programs (e.g., Microsoft Excel) that create 'Tab Delimited Text' and 'Comma Separated Values' (.csv) files typically use quotation marks to 'protect' certain characters (e.g, commas) when used in text (e.g., ...Oligochaeta;Stylaria;Stylaria_sp._aguinaldo,_1997) as they have the potential to be misread (e.g., causing a column split in a .csv file between 'aguinaldo' and '_1997'). To correct this issue, make sure that taxa in the taxonomic strings are separated with a semicolon (e.g., ...Ustilaginomycotina;Ustilago;Ustilago_maydis) rather than a comma and remove all commas from the text portion of the string (e.g., ...Oligochaeta;Stylaria;Stylaria_sp._aguinaldo_1997). After you have made this correction, you may also need to clear any quotation marks from your OTU table. Do this by opening the file in a text editor and then delete all the quotation marks (i.e., use the find/replace function to replace all quotes '"' with a blank '' - as in nothing, not a space - see note below).

- <b>Extra spaces</b>. Spaces can cause problems when a file is being read into a program, this is why they are typically replaced with an underscore in the taxonomic strings (e.g., 'Stylaria_sp.' in the above example). To correct this issue, open the OTU table in a text editor and remove space gaps (i.e., gaps that consist of more than a single space), and then clear all of the spaces (i.e., use the find/replace function to replace all spaces ' ' with an underscore '_'). <i><b>Note:</b> blank spaces in the file name can also cause problems for the FunGuild online version, so spaces in input file names should likewise be replaced by underscores (e.g., otu table.txt should be changed to otu_table.txt).</i>

***
<b>Papers Citing FunGuild</b>
<a href="https://scholar.google.com/scholar?hl=en&as_sdt=0%2C36&q=funguild&btnG=" target = '_blank'>Google Scholar</a>
