<h1>FUNGuild: Fungi + fUNctional + Guild</h1>

<b><i>Over 13,000 fungal taxa now included in the database</i>!</b>

<h3>Quick start</h3>

The FUNGuild.py script was written under Python 3 environment. If you don't have a Python 3 environment, we recommend to install Anaconda (https://www.anaconda.com/products/individual).

FUNGuild now takes two steps (parsers) for the functions of fungi. First we implemented a taxa parser to extract taxonomic information from the user provided OTU table. Then we use a guild parser to query the FUNGuild database. In this way, we can avoid most of the format issues we encountered when dealing with the original OTU table. You can also complie your own taxa file as the input for the guild parser.

Use -h or --help for a detail manual of FUNGuild.

    git clone https://github.com/UMNFuN/FUNGuild
    cd FUNGuild/
    python FUNGuild.py taxa -otu example/otu_table.txt -format tsv -column taxonomy -classifier unite
    python FUNGuild.py guild -taxa example/otu_table.taxa.txt

<b>Online version:</b><br>
http://funguild.org<br>

<b>Databases:</b><br>
http://stbates.org/funguild_db.php<br>
http://stbates.org/nemaguild_db.php<br>

<b>Api:</b><br>
api url = http://www.stbates.org/guilds/services/api/<br>
api url + query.php?qField=NAME OF DESIRED FIELD&qText=QUERY TEXT"<br>
e.g., http://www.stbates.org/guilds/services/api/query.php?qField=taxon&qText=Tulostoma<br>

<b>Citation:</b><br>
Nguyen NH, Song Z, Bates ST, Branco S, Tedersoo L, Menke J, Schilling JS, Kennedy PG. 2016. FUNGuild: An open annotation tool for parsing fungal community datasets by ecological guild. Fungal Ecology 20:241–248.<br> (https://cbs.umn.edu/sites/cbs.umn.edu/files/public/downloads/Nguyenetal2015b.pdf)

****

<b>Contributors:</b> Michelle Afkhami, Carlos Aguilar-Trigueros, Scott T. Bates, Sarah Branco, Posy Busby, Natalie Christian, Will Cornwell, Fukasawa Fu, Romina Gazis, Rannveig Jacobsen, Peter Kennedy, Daniel Lindner, Jon Menke, Amy Milo, Nhu Nguyen, Henrik Nilsson, Jonathan Schilling, Zewei Song, Jennifer Talbot, Leho Tedersoo, Nathaniel Tobey, and Amy Zanne

****

<b>IMPORTANT: Interpretation of data</b>
We highly recommend that users of FUNGuild read through the <a href="https://github.com/UMNFuN/FUNGuild/blob/master/FUNGuild_Manual.pdf">manual</a> and the <a href="https://cbs.umn.edu/sites/cbs.umn.edu/files/public/downloads/Nguyenetal2015b.pdf">paper</a> for suggestions on interpretation of your guild data.

****

<b>GENERAL NOTES</b>

The Guilds bioinformatic tool is a two-component system that includes online community annotated databases and a python script that assigns functional information to operational taxonomic units (OTUs) obtained from next generation sequencing of environmental samples. The script is based on an original in-house python script referenced in Branco et al. 2013. PLoS One 8:1–10 (http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0078295). It searches taxonomic strings in the user’s OTU table against the online Guilds databases (fungi or nematodes) containing taxonomic keywords and functional metadata. The output is the original OTU table with functional metadata appended, and users also have options to output an assigned OTUs only table and/or a table containing only OTUs for which assignments could not be made.

To run the Guilds bioinformatic tool locally, a current version of Python (https://www.python.org/) must be installed on the user’s local machine before the Guilds script (https://raw.githubusercontent.com/UMNFuN/FUNGuild/master/Guilds_v1.0.py) can be used. The Guilds databases are accessed by the python script remotely and, therefore, they do not need to be loaded to the user’s local machine. However, the script must be able to access the internet to connect with the databases.

An online version of the Guilds bioinformatic tool, the 'assignment application', is also available here:

http://funguild.org

An example OTU table .txt file to demonstrate formatting can be found <a href='http://www.stbates.org/guilds/download_examples.php/?download_file=otu_table_example.txt' target = '_blank'><i>here</i></a>.


<b>RUNNING THE SCRIPT LOCALLY FROM THE COMMAND LINE</b>

- Make sure you local computer has Python installed. Our current version of script support Python version higher than 2.7. We recommand that you install the Anaconda Python distribution for all required dependencies (https://www.anaconda.com/distribution/). Python 3.6 is prefered for its better support of Unicode characters (see https://www.python.org/downloads/).

- We use the Python package 'requests' for connecting with the FUNGuild database. This package should come with most of the common Python distributions. If you somehow don't have this package in your Python (i.e. you get this error: ImportError: No module named requests), you can install it using: pip install requests

- Download or copy the Guilds python script (https://raw.githubusercontent.com/UMNFuN/FUNGuild/master/Guilds_v1.1.py). The script should be saved in a file with the .py extension (e.g., Guilds_v1.1.py) rather than .txt (make sure that the hide extension setting is not activated, as the file might then actually save as e.g., Guilds_v1.1.py.txt).

- Open a terminal to run the script via command line (e.g., /Applications/Utilities/ and click on 'Terminal' for mac OR for Windows use Start or Start Menu and search for 'command' or 'cmd' and then click on the 'Command Prompt' icon). Be sure to follow any conventions (e.g., directory path formatting) that are relevant to your particular operating system.

- Next, cd (change directory in the command line) into folder (directory) where you saved your .py file containing the Guilds script (mac note - you can drag the desired folder from the finder into the terminal to get the directory path rather than having to type it). For example on mac, type something like this ```cd /Users/username/Documents/python_scripts``` into the terminal.

- Determine the path to your properly formatted (see above) OTU table (e.g., /Users/username/Documents/project/otu_table_example.txt).

- Make sure that your computer is connected to the Internet, as the script will need to access the online database of taxonomic key words.

- Make a Python call on the script (remember you should have already used the change directory command to cd into the folder that contains the script) giving the proper OTU table path (the -otu argument), desired taxonomic database (the -db argument; either ‘fungi’ or ‘nematode’; the default ‘fungi’ will be used if you don’t signify the -db argument), and desired output (add the argument -m to also output an OTU table with just the OTUs for which functional assignments could be made and/or -u to output a table with only OTUs that could not be assigned; a table that includes both the assigned and unassigned OTUs is the default output). For example on a mac, you would type something like this ```python Guilds_v1.0.py -otu /Users/username/Documents/project/otu_table_example.txt -db fungi -m -u``` into the terminal.

- Hit the enter/return key on your computer, and allow a few seconds for the script to do its magic!

****

<b><a name="contributing">CONTRIBUTING GUILD INFORMATION TO THE FUNGUILD DATABASE</a></b>

Data pertaining to particular fungal or nematode taxa can be submitted to the Guilds databases (FUNGuild_db or NEMAGuild_db) by contacting the database curators (xerantheum@gmail.com or scott.thomas.bates@gmail.com). All submitted entries will be reviewed by the database curators prior to being migrated to the main Guilds databases. Taxon entries proposed for addition to the databases will be accessable once they have been reviewed by the database curators and migrated to the main database. Once migrated, proposed entries will automatically be available to all using the Guilds bioinformatic tool to make annotated assignments to their OTU tables containing fungal or nematode taxa.

<b>Information should be entered into each Guilds database field, in sequence, as follows:</b>

- Taxon: The scientific name (e.g., Ganoderma).

- Taxon Level: A numeral corresponding the correct taxonomic level for the taxon (0 = keyword, 3 = Phylum, 4 = Subphylum, 5 = Class, 6 = Subclass, 7 = Order, 8 = Suborder, 9 = Family, 10 = Subfamily, 11 = Tribe, 12 = Subtribe, 13 = Genus, 15 = Subgenus, 16 = Section, 17 = Subsection, 18 = Series , 19 = Subseries, 20 = Species, 21 = Subspecies, 22 = Variety, 23 = Subvariety, 24 = Form, 25 = Subform, 26 = Form Species).

- Trophic Mode: One of three trophic categories [Pathotroph = receiving nutrients at the expense of the host cells and causing disease (e.g., biotroph, parasite, pathogen, etc.); Saprotroph = receiving nutrients by breaking down dead host cells (e.g., wood rotters, litter rotters, etc.); Symbiotroph = receiving nutrients by exchanging resources with host cells (e.g., ectomycorrhiza, lichens, etc.)]. The concepts presented here are similar to those of Tedersoo et al. 2014. Global diversity and geography of soil fungi. Science 346(6213). DOI: 10.1126/science.1256688 (http://www.sciencemag.org/content/346/6213/1256688).

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

<b><a name="troubleshooting">TROUBLESHOOTING</a></b>

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

- <b>Extra spaces</b>. Spaces can cause problems when a file is being read into a program, this is why they are typically replaced with an underscore in the taxonomic strings (e.g., 'Stylaria_sp.' in the above example). To correct this issue, open the OTU table in a text editor and remove space gaps (i.e., gaps that consist of more than a single space), and then clear all of the spaces (i.e., use the find/replace function to replace all spaces ' ' with an underscore '_'). <i><b>Note:</b> blank spaces in the file name can also cause problems for the FunGuild online version, so spaces in input file names should likewise be replaced by underscores (e.g., otu table.txt should be changed to otu_table.txt).</i>

<b>Online version of the script:</b> <s>The online Guilds_v1.0.py application (http://www.stbates.org/guilds/app.php) calls the python code from php when the 'Begin Analysis' button is 'pushed'. This application should work well for properly formatted (see above) OTU tables of a smaller file size (e.g., less than 25MB). There is a well known issue with php page time outs for processes that take a long time (read: more than the php default of 30 seconds). The script runs quickly, typically just a few seconds, but server handling of large files (e.g., loading them through your browser) can take time. To allow time for script processes to complete, the php 'max_execution_time' has been set to 0 (i.e., no time limit). Even though removing this restriction should allow time for processes to complete, large files can cause other problems that will trip a 500 'Internal Server Error' flag.</s>

<s>When working with large OTU table files, consider the following:</s>

<s>- Zip OTU tables of a larger file size (e.g., over 10MB) before loading them onto the server. This approach has been tested with larger files and seems to be in working order; however, processing time is slowed considerably (which shouldn't be an issue for php page time outs - see above). You can always try larger OTU table sizes (up to 50MB when zipped), but a great deal of patience may be required. This being said, it is recommended that you use a local version of the program run from the command line to run the script (see below).</s>

<s>- Run the script locally. Running the script from your local computer via command line (see above) will eliminate server related issues, remove the need to zip the file, and should speed up processing times (files of 25MB or more will typically run in several seconds).</s>

<b>Papers Citing FunGuild</b>

<b>2019</b>

Adamczyk M, Hagedorn F, Wipf S, Donhauser J, Vittoz P, Rixen C, Frossard A, Theurillat J-P, Frey B. 2019. The soil microbiome of Gloria Mountain summits in the Swiss Alps. Frontiers in Microbiology 10:e1080. https://doi.org/10.3389/fmicb.2019.01080

Adl SM, Bass D, Lane CE, Lukeš J, Schoch CL, Smirnov A, Agatha S, Berney C, Brown MW, Burki F, Cárdenas P, Čepička I, Chistyakova L, del Campo J, Dunthorn M, Edvardsen B, Eglit Y, Guillou L, Hampl V, Heiss AA, Hoppenrath M, James TY, Karnkowska A, Karpov S, Kim E, Kolisko M, Kudryavtsev A, Lahr DJG, Lara E, Le Gall L, Lynn DH, Mann DG, Massana R, Mitchell EAD, Morrow C, Park JS, Pawlowski JW, Powell MJ, Richter DJ. Rueckert S, Shadwick L, Shimano S, Spiegel FW, Torruella G, Youssef N, Zlatogursky V, Zhang Q. 2019. Revisions to the classification nomenclature and diversity of Eukaryotes. Journal of Eukaryotic Microbiology 66:4-119. https://doi.org/10.1111/jeu.12691

Aguilar-Trigueros CA, Hempel S, Powell JR, Cornwell WK, Rillig MC. 2019. Bridging reproductive and microbial ecology:a case study in arbuscular mycorrhizal fungi. ISME Journal 13:873-884. https://doi.org/10.1038/s41396-018-0314-7

Alzarhani AK, Clark DR, Underwood GJC, Ford H, Cotton TEA, Dumbrell AJ. 2019. Are drivers of root-associated fungal community structure context specific? ISME Journal 13:1330-1344. https://doi.org/10.1038/s41396-019-0350-y

Ampt EA, van Ruijven J, Raaijmakers JM, Termorshuizen AJ, Mommer L. 2019. Linking ecology and plant pathology to unravel the importance of soil-borne fungal pathogens in species-rich grasslands. European Journal of Plant Pathology 154:141-156. https://doi.org/10.1007/s10658-018-1573-x

Andrew C, Büntgen U, Egli S, Senn-Irlet B, Grytnes J-A, Heilmann-Clausen J, Boddy L, Bässler C, Gange AC, Heegaard E, Høiland K, Kirk PM, Krisai-Greilhüber I, Kuyper TW, Kauserud H. 2019. Open-source data reveal how collections-based fungal diversity is sensitive to global change. Applications in Plant Sciences 7:e01227. https://doi.org/10.1002/aps3.1227

Anthony MA, Stinson KA, Trautwig AN, Coates-Connor E, Frey SD. 2019. Fungal communities do not recover after removing invasive <i>Alliaria petiolata</i> (garlic mustard). Biological Invasions. https://doi.org/10.1007/s10530-019-02031-8

Archer SDJ, Lee KC, Caruso T, Maki T, Lee CK, Cary SC, Cowan DA, Maestre FT, Pointing SB. 2019. Airborne microbial transport limitation to isolated Antarctic soil habitats. Nature Microbiology 4:925-932. https://doi.org/10.1038/s41564-019-0370-4Castaño C, Dejene T, Mediavilla O, Geml J, Oria-de-Rueda JA, Martín-Pinto P. 2019. Changes in fungal diversity and composition along a chronosequence of Eucalyptus grandis plantations in Ethiopia. Fungal Ecology 39:328-335. https://doi.org/10.1016/j.funeco.2019.02.003

Asplund J, Kauserud H, Ohlson M, Nybakken L. 2019. Spruce and beech as local determinants of forest fungal community structure in litter humus and mineral soil. FEMS Microbiology Ecology 95:fiy232. https://doi.org/10.1093/femsec/fiy232

Awad A, Majcherczyk A, Schall P, Schröter K, Schöning I, Schrumpf M, Ehbrecht M, Boch S, Kahl T, Bauhus J, Seidel D, Ammer C, Fischer M, Kües U, Pena R. 2019. Ectomycorrhizal and saprotrophic soil fungal biomass are driven by different factors and vary among broadleaf and coniferous temperate forests. Soil Biology and Biochemistry 131:9-18. https://doi.org/10.1016/j.soilbio.2018.12.014

Boeraeve M, Honnay O, Jacquemyn H. 2019. Forest edge effects on the mycorrhizal communities of the dual-mycorrhizal tree species Alnus glutinosa (L.) Gaertn. Science of the Total Environment 666:703-712. https://doi.org/10.1016/j.scitotenv.2019.02.290

Borg Dahl M, Brejnrod AD, Russel J, Sørensen SJ, Schnittler M. 2019. Different degrees of niche differentiation for Bacteria Fungi and Myxomycetes within an elevational transect in the German Alps. Microbial Ecology. https://doi.org/10.1007/s00248-019-01347-1

Bruns TD. 2019. The developing relationship between the study of fungal communities and community ecology theory. Fungal Ecology 39:393-402. https://doi.org/10.1016/j.funeco.2018.12.009

Chen J, Xu H, He D, Li Y, Luo T, Yang H, Lin M. 2019. Historical logging alters soil fungal community composition and network in a tropical rainforest. Forest Ecology and Management 433:228-239. https://doi.org/10.1016/j.foreco.2018.11.005

Chen L, Xiang W, Wu H, Ouyang S, Zhou B, Zeng Y, Chen Y, Kuzyakov Y. 2019. Tree species identity surpasses richness in affecting soil microbial richness and community composition in subtropical forests. Soil Biology and Biochemistry 130:113-121. https://doi.org/10.1016/j.soilbio.2018.12.008

Chen Y, Jia P, Cadotte MW, Wang P, Liu X, Qi Y, Jiang X, Wang Z, Shu W. 2019. Rare and phylogenetically distinct plant species exhibit less diverse root-associated pathogen communities. Journal of Ecology 107 (3):1226-1237. https://doi.org/10.1111/1365-2745.13099

Cleary M, Oskay F, Doğmuş HT, Lehtijärvi A, Woodward S, Vettraino AM. 2019. Cryptic risks to forest biosecurity associated with the global movement of commercial seed. Forests 10:e459. https://doi.org/10.3390/f10050459

Dai H, Zhang H, Xue Y, Gao Y, Qian X, Zhao H, Cheng H, Li Z, Liu K. 2019. Response of fungal community and function to different tillage and straw returning methods. Scientia Agricultura Sinica 52:2280-2294. https://doi.org/10.3864/j.issn.0578-1752.2019.13.008

Dukes AE, Koyama A, Dunfield KE, Antunes PM. 2019. Enemy of my enemy: evidence for variable soil biota feedbacks of <i>Vincetoxicum rossicum</i> on native plants. Biological Invasions 21:67-83. https://doi.org/10.1007/s10530-018-1804-2

Egidi E, Wood JL, Celestina C, May TW, Mele P, Edwards J, Powell J, Bissett A, Franks AE. 2019. Delving into the dark ecology: A continent-wide assessment of patterns of composition in soil fungal communities from Australian tussock grasslands. Fungal Ecology 39:356-370. https://doi.org/10.1016/j.funeco.2019.03.001

Feng H, Wang S, Gao Z, Wang Z, Ren X, Hu S, Pan H. 2019. Effect of land use on the composition of bacterial and fungal communities in saline–sodic soils. Land Degradation and Development. https://doi.org/10.1002/ldr.3386

Franić I, Prospero S, Hartmann M, Allan E, Auger-Rozenberg M-A, Grünwald NJ, Kenis M, Roques A, Schneider S, Sniezko R, Williams W, Eschen R. 2019. Are traded forest tree seeds a potential source of nonnative pests? Ecological Applications. https://doi.org/10.1002/eap.1971

Geml J. 2019. Soil fungal communities reflect aspect-driven environmental structuring and vegetation types in a Pannonian forest landscape. Fungal Ecology 39:63-79. https://doi.org/10.1016/j.funeco.2018.12.005

Gora EM, Lucas JM, Yanoviak SP. 2019. Microbial composition and wood decomposition rates vary with microclimate from the ground to the canopy in a tropical forest. Ecosystems. https://doi.org/10.1007/s10021-019-00359-9

Grove S, Saarman NP, Gilbert GS, Faircloth B, Haubensak KA, Parker IM. 2019. Ectomycorrhizas and tree seedling establishment are strongly influenced by forest edge proximity but not soil inoculum. Ecological Applications 29:e01867. https://doi.org/10.1002/eap.1867

Guo Y, Hou L, Zhang Z, Zhang J, Cheng J, Wei G, Lin Y. 2019 Soil microbial diversity during 30 years of grassland restoration on the Loess Plateau China:Tight linkages with plant diversity. Land Degradation and Development 30:1172-1182. https://doi.org/10.1002/ldr.3300

Gupta VVSR, Bramley RGV, Greenfield P, Yu J, Herderich MJ. 2019. Vineyard soil microbiome composition related to rotundone concentration in Australian cool climate 'peppery' Shiraz grapes. Frontiers in Microbiology 10:e1607. https://doi.org/10.3389/fmicb.2019.01607

Hoch JMK, Rhodes ME, Shek KL, Dinwiddie D, Hiebert TC, Gill AS, Estrada AES, Griffin KL, Palmer MI, McGuire KL. 2019. Soil microbial assemblages are linked to plant community composition and contribute to ecosystem services on urban green roofs. Frontiers in Ecology and Evolution 7:198. https://doi.org/10.3389/fevo.2019.00198

Hofstetter V, Buyck B, Eyssartier G, Schnee S, Gindro K. 2019. The unbearable lightness of sequenced-based identification. Fungal Diversity 96:243-284. https://doi.org/10.1007/s13225-019-00428-3

Hu Y, Veresoglou SD, Tedersoo L, Xu T, Ge T, Liu L, Chen Y, Hao Z, Su Y, Rillig MC, Chen B. 2019. Contrasting latitudinal diversity and co-occurrence patterns of soil fungi and plants in forest ecosystems. Soil Biology and Biochemistry 131:100-110. https://doi.org/10.1016/j.soilbio.2019.01.001

Ji N-N, Gao C, Sandel B, Zheng Y, Chen L, Wu B-W, Li X-C, Wang Y-L, Peng-Peng Lü, Sun X, Guo L-D. 2019. Late Quaternary climate change explains soil fungal community composition rather than fungal richness in forest ecosystems. Ecology and Evolution 9:6678-6692. https://doi.org/10.1002/ece3.5247

Kerfahi D, Ogwu MC, Ariunzaya D, Balt A, Davaasuren D, Enkhmandal O, Purevsuren T, Batbaatar A, Tibbett M, Undrakhbold S, Boldgiv B, Adams JM. 2019. Metal-tolerant fungal communities are delineated by high zinc lead and copper concentrations in metalliferous Gobi Desert soils. Microbial Ecology. https://doi.org/10.1007/s00248-019-01405-8

Kivlin SN, Kazenel MR, Lynn JS, Lee Taylor D, Rudgers JA. 2019. Plant identity influences foliar fungal symbionts more than elevation in the Colorado Rocky Mountains. Microbial Ecology. https://doi.org/10.1007/s00248-019-01336-4

Kong X, Jin D, Wang X, Zhang F, Duan G, Liu H, Jia M, Deng Y. 2019. Dibutyl phthalate contamination remolded the fungal community in agro-environmental system. Chemosphere 215:189-198. https://doi.org/10.1016/j.chemosphere.2018.10.020

Lajoie G, Kembel SW. 2019. Making the most of trait-based approaches for microbial ecology. Trends in Microbiology. https://doi.org/10.1016/j.tim.2019.06.003

Lee MR, Powell JR, Oberle B, Cornwell WK, Lyons M, Rigg JL, Zanne AE. Good neighbors aplenty: Fungal endophytes rarely exhibit competitive exclusion patterns across a span of woody habitats. Ecology. https://doi.org/10.1002/ecy.2790

Leff JW, Bardgett RD, Wilkinson A, Jackson BG, Pritchard WJ, De Long JR, Oakley S, Mason KE, Ostle NJ, Johnson D, Baggs EM, Fierer N. 2019. Predicting the structure of soil communities from plant community taxonomy phylogeny and traits. ISME Journal 12:1794-1805. https://doi.org/10.1038/s41396-018-0089-x

Legrand F, Chen W, Cobo-Díaz JF, Picot A, Le Floch G. 2019. Co-occurrence analysis reveal that biotic and abiotic factors influence soil fungistasis against <i>Fusarium graminearum</i>. FEMS Microbiology Ecology 95:fiz056. https://doi.org/10.1093/femsec/fiz056

Li D, Li X, Su Y, Li X, Yin H, Li X, Guo M, He Y. 2019. Forest gaps influence fungal community assembly in a weeping cypress forest. Applied Microbiology and Biotechnology 103:3215-3224. https://doi.org/10.1007/s00253-018-09582-1

Li P, Yang L, Li G, Xu H, Wang Y, Li Z. 2019. Research of rhizosphere fungi communities of <i>Fusarium</i> root rot diseased tobacco based on FUNGuild. Acta Tabacaria Sinica 25:63-68. https://doi.org/10.16472/j.chinatobacco.2018.242

Li W, Wang M, Burgaud G, Yu H, Cai L. 2019. Fungal community composition and potential depth-related driving factors impacting distribution pattern and trophic modes from epi- to abysso-pelagic zones of the Western Pacific Ocean. Microbial Ecology. https://doi.org/10.1007/s00248-019-01374-y

Li Y, Jiang L, Lv W, Cui S, Zhang L, Wang Q, Meng F, Li B, Liu P, Suonan J, Renzeng W, Li X, Luo C, Zhang Z, Dorji T, Wang Y, Wang S. 2019. Fungal pathogens pose a potential threat to animal and plant health in desertified and pika-burrowed alpine meadows on the tibetan plateau. Canadian Journal of Microbiology 65:365-376. https://doi.org/10.1139/cjm-2018-0338

Li Y, Nie C, Liu Y, Du W, He P. 2019. Soil microbial community composition closely associates with specific enzyme activities and soil carbon chemistry in a long-term nitrogen fertilized grassland. Science of the Total Environment 654:264-274. https://doi.org/10.1016/j.scitotenv.2018.11.031

Lian T, Mu Y, Jin J, Ma Q, Cheng Y, Cai Z, Nian H. 2019. Impact of intercropping on the coupling between soil microbial community structure activity and nutrient-use efficiencies. PeerJ 2019:e6412. https://doi.org/10.7717/peerj.6412

Liao H-L, Bonito G, Rojas JA, Hameed K, Wu S, Schadt CW, Labbé J, Tuskan GA, Martin F, Grigoriev IV, Vilgalys R. 2019. Fungal endophytes of <i>Populus trichocarpa</i> alter host phenotype gene expression and rhizobiome composition. Molecular Plant-Microbe Interactions 31:853-864. https://doi.org/10.1094/MPMI-05-18-0133-R

Liu H, Pan F, Han X, Song F, Zhang Z, Yan J, Xu Y. 2019. Response of soil fungal community structure to long-term continuous soybean cropping. Frontiers in Microbiology 10:e3316. https://doi.org/10.3389/fmicb.2018.03316

Liu J, Yao Q, Li Y, Zhang W, Mi G, Chen X, Yu Z, Wang G. 2019. Continuous cropping of soybean alters the bulk and rhizospheric soil fungal communities in a Mollisol of Northeast PR China. Land Degradation and Development. https://doi.org/10.1002/ldr.3378

Liu T, He J, Cui C, Tang J. 2019. Exploiting community structure interactions and functional characteristics of fungi involved in the biodrying of storage sludge and beer lees. Journal of Environmental Management 232:321-329. https://doi.org/10.1016/j.jenvman.2018.11.089

Lofgren LA, Uehling JK, Branco S, Bruns TD, Martin F, Kennedy PG. 2019. Genome-based estimates of fungal rDNA copy number variation across phylogenetic scales and ecological lifestyles. Molecular Ecology 28:721-730. https://doi.org/10.1111/mec.14995

Luis P, Saint-Genis G, Vallon L, Bourgeois C, Bruto M, Marchand C, Record E, Hugoni M. 2019. Contrasted ecological niches shape fungal and prokaryotic community structure in mangroves sediments. Environmental Microbiology 21:1407-1424. https://doi.org/10.1111/1462-2920.14571

Lüneberg K, Schneider D, Brinkmann N, Siebe C, Daniel R. 2019. Land use change and water quality use for irrigation alters drylands soil fungal community in the Mezquital Valley Mexico. Frontiers in Microbiology 10:e1220. https://doi.org/10.3389/fmicb.2019.01220

Martinez-Almoyna C, Thuiller W, Chalmandrier L, Ohlmann M, Foulquier A, Clément J-C, Zinger L, Münkemüller T. 2019. Multi-trophic β-diversity mediates the effect of environmental gradients on the turnover of multiple ecosystem functions. Functional Ecology. https://doi.org/10.1111/1365-2435.13393

Miller EC, Perron GG, Collins CD. 2019. Plant-driven changes in soil microbial communities influence seed germination through negative feedbacks. Ecology and Evolution. https://doi.org/10.1002/ece3.5476

Morales-Rodríguez C, Anslan S, Auger-Rozenberg M-A, Augustin S, Baranchikov Y, Bellahirech A, Burokiene D, Čepukoit D, Çota E, Davydenko K, Lehtijärvi HTD, Drenkhan R, Drenkhan T, Eschen R, Franić I, Glavendekić M, de Groot M, Kacprzyk M, Kenis M, Kirichenko N, Matsiakh I, Musolin DL, Nowakowska JA, O'Hanlon R, Prospero S, Roques A, Santini A, Talgø V, Tedersoo L, Uimari A, Vannini A, Witzell J, Woodward S, Zambounis A, Cleary M. 2019. Forewarned is forearmed: Harmonized approaches for early detection of potentially invasive pests and pathogens in sentinel plantings. NeoBiota 47:95-123. https://doi.org/10.3897/neobiota.47.34276

Morrison EW, Pringle A, van Diepen LTA, Grandy AS, Melillo JM, Frey SD. 2019. Warming alters fungal communities and litter chemistry with implications for soil carbon stocks. Soil Biology and Biochemistry 132:120-130. https://doi.org/10.1016/j.soilbio.2019.02.005

Nilsson RH, Anslan S, Bahram M, Wurzbacher C, Baldrian P, Tedersoo L. 2019. Mycobiome diversity:high-throughput sequencing and identification of fungi. Nature Reviews Microbiology 17:95-109. https://doi.org/10.1038/s41579-018-0116-y

Nilsson RH, Larsson K-H, Taylor AFS, Bengtsson-Palme J, Jeppesen TS, Schigel D, Kennedy P, Picard K, Glöckner FO, Tedersoo L, Saar I, Kõljalg U, Abarenkov K. 2019. The UNITE database for molecular identification of fungi: Handling dark taxa and parallel taxonomic classifications. Nucleic Acids Research 47:D259-D264. https://doi.org/10.1093/nar/gky1022

Ning C, Mueller GM, Egerton-Warburton LM, Xiang W, Yan W. 2019. Host phylogenetic relatedness and soil nutrients shape ectomycorrhizal community composition in native and exotic pine plantations. Forests 10:e263. https://doi.org/10.3390/f10030263

Noreika N, Helm A, Öpik M, Jairus T, Vasar M, Reier Ü, Kook E, Riibak K, Kasari L, Tullus H, Tullus T, Lutter R, Oja E, Saag A, Randlane T, Pärtel M. 2019. Forest biomass soil and biodiversity relationships originate from biogeographic affinity and direct ecological effects. Oikos. https://doi.org/10.1111/oik.06693

Nuske SJ, Anslan S, Tedersoo L, Congdon BC, Abell SE. 2019. Ectomycorrhizal fungal communities are dominated by mammalian dispersed truffle-like taxa in north-east Australian woodlands. Mycorrhiza. https://doi.org/10.1007/s00572-019-00886-2

Ortega-Arbulú A-S, Pichler M, Vuillemin A, Orsi WD. 2019. Effects of organic matter and low oxygen on the mycobenthos in a coastal lagoon. Environmental Microbiology 21:374-388. https://doi.org/10.1111/1462-2920.14469

Palmieri F, Estoppey A, House GL, Lohberger A, Bindschedler S, Chain PSG, Junier P. 2019. Oxalic acid a molecule at the crossroads of bacterial-fungal interactions. Advances in Applied Microbiology 106:49-77. https://doi.org/10.1016/bs.aambs.2018.10.001

Pec GJ, Scott NM, Hupperts SF, Hankin SL, Landhäusser SM, Karst J. 2019. Restoration of belowground fungal communities in reclaimed landscapes of the Canadian boreal forest. Restoration Ecology. https://doi.org/10.1111/rec.12990

Penone C, Allan E, Soliveres S, Felipe-Lucia MR, Gossner MM, Seibold S, Simons NK, Schall P, van der Plas F, Manning P, Manzanedo RD, Boch S, Prati D, Ammer C, Bauhus J, Buscot F, Ehbrecht M, Goldmann K, Jung K, Müller J, Müller JC, Pena R, Polle A, Renner SC, Ruess L, Schönig I, Schrumpf M, Solly EF, Tschapka M, Weisser WW, Wubet T, Fischer M. 2019. Specialisation and diversity of multiple trophic groups are promoted by different forest features. Ecology Letters 22:170-180. https://doi.org/10.1111/ele.13182

Purahong W, Mapook A, Wu Y-T, Chen C-T. 2019. Characterization of the <i>Castanopsis carlesii</i> deadwood mycobiome by PacBio sequencing of the full-length fungal nuclear ribosomal internal transcribed spacer (ITS). Frontiers in Microbiology 10:e983. https://doi.org/10.3389/fmicb.2019.00983

Qian X, Li H, Wang Y, Wu B, Wu M, Chen L, Li X, Zhang Y, Wang X, Shi M, Zheng Y, Guo L, Zhang D. 2019. Leaf and Root Endospheres Harbor Lower Fungal Diversity and Less Complex Fungal Co-occurrence Patterns Than Rhizosphere. Frontiers in Microbiology 10:e1015. https://doi.org/10.3389/fmicb.2019.01015

Ramirez KS, Snoek LB, Koorem K, Geisen S, Bloem LJ, ten Hooven F, Kostenko O, Krigas N, Manrubia M, Caković D, van Raaij D, Tsiafouli MA, Vreš B, Čelik T, Weser C, Wilschut RA, van der Putten WH. 2019. Range-expansion effects on the belowground plant microbiome. Nature Ecology and Evolution 3:604-611. https://doi.org/10.1038/s41559-019-0828-z

Schmidt R, Mitchell J, Scow K. 2019. Cover cropping and no-till increase diversity and symbiotroph: saprotroph ratios of soil fungal communities. Soil Biology and Biochemistry 129:99-109. https://doi.org/10.1016/j.soilbio.2018.11.010

Schröter K, Wemheuer B, Pena R, Schöning I, Ehbrecht M, Schall P, Ammer C, Daniel R, Polle A. 2019. Assembly processes of trophic guilds in the root mycobiome of temperate forests. Molecular Ecology 28:348-364. https://doi.org/10.1111/mec.14887

Seibold S. Müller J. Baldrian P. Cadotte M.W. Štursová M. Biedermann P.H.W. Krah F.-S. Bässler C. 2019. Fungi associated with beetles dispersing from dead wood – Let's take the beetle bus!. Fungal Ecology 39:100-108. https://doi.org/10.1016/j.funeco.2018.11.016

Sha SP, Suryavanshi MV, Tamang JP. 2019. Mycobiome diversity in traditionally prepared starters for alcoholic beverages in India by high-throughput sequencing method. Frontiers in Microbiology 10:e348. https://doi.org/10.3389/fmicb.2019.00348

Shi S, Chang J, Tian L, Nasir F, Ji L, Li X, Tian C. 2019. Comparative analysis of the rhizomicrobiome of the wild versus cultivated crop:insights from rice and soybean. Archives of Microbiology. https://doi.org/10.1007/s00203-019-01638-8

Singer D, Metz S, Unrein F, Shimano S, Mazei Y, Mitchell EAD, Lara E. 2019. Contrasted micro-Eukaryotic diversity associated with sphagnum mosses in tropical subtropical and temperate climatic zones. Microbial Ecology. https://doi.org/10.1007/s00248-019-01325-7

Sorensen PO, Bhatnagar JM, Christenson L, Duran J, Fahey T, Fisk MC, Finzi AC, Groffman PM, Morse JL, Templer PH. 2019. Roots mediate the effects of snowpack decline on soil bacteria fungi and nitrogen cycling in a northern hardwood forest. Frontiers in Microbiology 10:e926. https://doi.org/10.3389/fmicb.2019.00926

Sundaresan N, Jagan EG, Kathamuthu G, Pandi M. 2019. Internal transcribed spacer 2 (ITS2) molecular morphometric analysis based species delimitation of foliar endophytic fungi from <i>Aglaia elaeagnoidea</i>, <i>Flacourtia inermis</i> and <i>Premna serratifolia</i>. PLoS ONE 14:e0215024. https://doi.org/10.1371/journal.pone.0215024

Tatsumi C, Taniguchi T, Du S, Yamanaka N, Tateno R. 2019. The steps in the soil nitrogen transformation process vary along an aridity gradient via changes in the microbial community. Biogeochemistry 144:15-29. https://doi.org/10.1007/s10533-019-00569-2

Tayyab M, Islam W, Lee CG, Pang Z, Khalil F, Lin S, Lin W, Zhang H. 2019. Short-term effects of different organic amendments on soil fungal composition. Sustainability (Switzerland) 11:e198. https://doi.org/10.3390/su11010198

Tedersoo L, Drenkhan R, Anslan S, Morales-Rodriguez C, Cleary M. 2019. High-throughput identification and diagnostics of pathogens and pests: Overview and practical recommendations. Molecular Ecology Resources 19:47-76. https://doi.org/10.1111/1755-0998.12959

Toju H, Kurokawa H, Kenta T. 2019. Factors influencing leaf- and root-associated communities of bacteria and fungi across 33 plant orders in a grassland. Frontiers in Microbiology 10:e241. https://doi.org/10.3389/fmicb.2019.00241

Torres-Andrade P, Cappellazzi J, Morrell JJ. 2019. Fungal colonization patterns of wood exposed out of soil contact in Western Oregon. International Biodeterioration and Biodegradation 137:14-22. https://doi.org/10.1016/j.ibiod.2018.11.005

Truong C, Gabbarini LA, Corrales A, Mujic AB, Escobar JM, Moretto A, Smith ME. 2019. Ectomycorrhizal fungi and soil enzymes exhibit contrasting patterns along elevation gradients in southern Patagonia. New Phytologist 222:1936-1950. https://doi.org/10.1111/nph.15714

Veen GFC, Snoek BL, Bakx-Schotman T, Wardle DA, van der Putten WH. 2019. Relationships between fungal community composition in decomposing leaf litter and home-field advantage effects. Functional Ecology. https://doi.org/10.1111/1365-2435.13351

Wang L, Delgado-Baquerizo M, Wang D, Isbell F, Liu J, Feng C, Liu J, Zhong Z, Zhu H, Yuan X, Chang Q, Liu C. 2019. Diversifying livestock promotes multidiversity and multifunctionality in managed grasslands. Proceedings of the National Academy of Sciences of the United States of America 116:6187-6192. https://doi.org/10.1073/pnas.1807354116

Wang M, Ruan W, Kostenko O, Carvalho S, Hannula SE, Mulder PPJ, Bu F, van der Putten WH, Bezemer TM. 2019. Removal of soil biota alters soil feedback effects on plant growth and defense chemistry. New Phytologist 221:1478-1491. https://doi.org/10.1111/nph.15485

Wang M, Tian J, Bu Z, Lamit LJ, Chen H, Zhu Q, Peng C. 2019. Structural and functional differentiation of the microbial community in the surface and subsurface peat of two minerotrophic fens in China. Plant and Soil 437:21-40. https://doi.org/10.1007/s11104-019-03962-w

Wang P, Chen Y, Sun Y, Tan S, Zhang S, Wang Z, Zhou J, Zhang G, Shu W, Luo C, Kuang J. 2019. Distinct biogeography of different fungal guilds and their associations with plant species richness in forest ecosystems. Frontiers in Ecology and Evolution 7:e216. https://doi.org/10.3389/fevo.2019.00216

Wu D, Zhang M, Peng M, Sui X, Li W, Sun G. 2019. Variations in soil functional fungal community structure associated with pure and mixed plantations in typical temperate forests of China. Frontiers in Microbiology 10:e1636. https://doi.org/10.3389/fmicb.2019.01636

Wu H, Xiang W, Ouyang S, Forrester DI, Zhou B, Chen L, Ge T, Lei P, Chen L, Zeng Y, Song X, Peñuelas J, Peng C. 2019. Linkage between tree species richness and soil microbial diversity improves phosphorus bioavailability. Functional Ecology. https://doi.org/10.1111/1365-2435.13355

Wutkowska M, Vader A, Mundra S, Cooper EJ, Eidesen PB. 2019. Dead or alive; Or does it really matter? Level of congruency between trophic modes in total and active fungal communities in high arctic soil. Frontiers in Microbiology 10:e3243. https://doi.org/10.3389/fmicb.2018.03243

Xiao W, Chen HYH, Kumar P, Chen C, Guan Q. 2019. Multiple interactions between tree composition and diversity and microbial diversity underly litter decomposition. Geoderma 341:161-171. https://doi.org/10.1016/j.geoderma.2019.01.045

Xiao W, Zhao J, Yan X, Guan Q. 2019. Tree Diversity Determines the Diversity of the Taxonomic and Functional Structure of the Fungal Community in Forest Litter in Southern China. Forest Science 65:40-47. https://doi.org/10.1093/forsci/fxy037

Xu W, Gao Y-H, Gong L-F, Li M, Pang K-L, Luo Z-H. 2019. Fungal diversity in the deep-sea hadal sediments of the Yap Trench by cultivation and high throughput sequencing methods based on ITS rRNA gene. Deep-Sea Research Part I:Oceanographic Research Papers 145:125-136. https://doi.org/10.1016/j.dsr.2019.02.001

Yang J, Dong C, Chen W, Liang J, Han Y, Liang Z. 2019. Community composition and ecological functional structural analysis of endophytic fungi in bark of <i>Eucommia ulmoides</i> in different areas. Zhongguo Zhongyao Zazhi 44:1126-1134. https://doi.org/10.19540/j.cnki.cjcmm.20181226.005

Yang T, Tedersoo L, Soltis PS, Soltis DE, Gilbert JA, Sun M, Shi Y, Wang H, Li Y, Zhang J, Chen Z, Lin H, Zhao Y, Fu C, Chu H. 2019. Phylogenetic imprint of woody plants on the soil mycobiome in natural mountain forests of eastern China. ISME Journal 13:686-697. https://doi.org/10.1038/s41396-018-0303-x

Yang W, Jeelani N, Xia L, Zhu Z, Luo Y, Cheng X, An S. 2019. Soil fungal communities vary with invasion by the exotic <i>Spartina alternifolia</i> Loisel. in coastal salt marshes of eastern China. Plant and Soil. https://doi.org/10.1007/s11104-019-04184-w

Yang W, Jing X, Guan Y, Zhai C, Wang T, Shi D, Sun W, Gu S. 2019. Response of fungal communities and co-occurrence network patterns to compost amendment in black soil of northeast China. Frontiers in Microbiology 10:e1562. https://doi.org/10.3389/fmicb.2019.01562

Zhang W-H, Sun R-B, Xu L, Liang J-N, Wu T-Y, Zhou J. 2019. Effects of micro-/nano-hydroxyapatite and phytoremediation on fungal community structure in copper contaminated soil. Ecotoxicology and Environmental Safety 174:100-109. https://doi.org/10.1016/j.ecoenv.2019.02.048

Zhang X, Zhong Z, Gai X, Ying J, Li W, Du X, Bian F, Yang C. 2019. Leaf-associated shifts in bacterial and fungal communities in response to chicken rearing under moso bamboo forests in subtropical China. Forests 10:e216. https://doi.org/10.3390/f10030216

Zhang Y, Li Q, Chen Y, Dai Q, Hu J. 2019. Mudflat reclamation causes change in the composition of fungal communities under long-term rice cultivation. Canadian Journal of Microbiology 65:530-537. https://doi.org/10.1139/cjm-2019-0005


<b>2018</b>

Abarenkov K, Somervuo P, Nilsson RH, Kirk PM, Huotari T, Abrego N, Ovaskainen O. 2018. Protax-fungi: A web-based tool for probabilistic taxonomic placement of fungal internal transcribed spacer sequences. New Phytologist 220:517-525. https://doi.org/10.1111/nph.15301

Abdelfattah A, Malacrinò A, Wisniewski M, Cacciola SO, Schena L. 2018. Metabarcoding: A powerful tool to investigate microbial communities and shape future plant protection strategies. Biological Control 120:1-10. https://doi.org/10.1016/j.biocontrol.2017.07.009

Amma S, Toju H, Wachrinrat C, Sato H, Tanabe AS, Artchawakom T, Kanzaki M. 2018. Composition and diversity of soil fungi in dipterocarpaceae-dominated seasonal tropical forests in Thailand. Microbes and Environments 33:135-143. https://doi.org/10.1264/jsme2.ME17168

Anslan S, Bahram M, Tedersoo L. 2018. Seasonal and annual variation in fungal communities associated with epigeic springtails (<i>Collembola s:</i>) in boreal forests. Soil Biology and Biochemistry 116:245-252. https://doi.org/10.1016/j.soilbio.2017.10.021

Argüelles-Moyao A, Garibay-Orijel R. 2018. Ectomycorrhizal fungal communities in high mountain conifer forests in central Mexico and their potential use in the assisted migration of <i>Abies religiosa</i>. Mycorrhiza 28:509-521. https://doi.org/10.1007/s00572-018-0841-0

Barnes CJ, van der Gast CJ, McNamara NP, Rowe R, Bending GD. 2018. Extreme rainfall affects assembly of the root-associated fungal community. New Phytologist 220:1172-1184. https://doi.org/10.1111/nph.14990

Bates ST, Miller AN, the Macrofungi Collections and Microfungi Collections Consortia. 2018. The protochecklist of North American nonlichenized Fungi. Mycologia 110:1222-1348. https://doi.org/10.1080/00275514.2018.1515410

Bhatnagar JM, Peay KG, Treseder KK. 2018. Litter chemistry influences decomposition through activity of specific microbial functional guilds. Ecological Monographs 88:429-444. https://doi.org/10.1002/ecm.1303

Bickford WA, Goldberg DE, Kowalski KP, Zak D.R. 2018. Root endophytes and invasiveness: No difference between native and non-native Phragmites in the Great Lakes Region. Ecosphere 9:e02526. https://doi.org/10.1002/ecs2.2526

Boeraeve M, Honnay O, Jacquemyn H. 2018. Effects of host species environmental filtering and forest age on community assembly of ectomycorrhizal fungi in fragmented forests. Fungal Ecology 36:89-98. https://doi.org/10.1016/j.funeco.2018.08.003

Brunner I, Fischer M, Rüthi J, Stierli B, Frey B. 2018. Ability of fungi isolated from plastic debris floating in the shoreline of a lake to degrade plastics. PLoS ONE 13:e0202047. https://doi.org/10.1371/journal.pone.0202047

Castaño C, Alday JG, Lindahl BD, Martínez de Aragón J, de-Miguel S, Colinas C, Parladé J, Pera J, Bonet JA. 2018. Lack of thinning effects over inter-annual changes in soil fungal community and diversity in a Mediterranean pine forest. Forest Ecology and Management 424:420-427. https://doi.org/10.1016/j.foreco.2018.05.004

Cazzolla Gatti R, Dudko A, Lim A, Velichevskaya AI, Lushchaeva IV, Pivovarova AV, Ventura S, Lumini E, Berruti A, Volkov IV. 2018. The last 50 years of climate-induced melting of the Maliy Aktru glacier (Altai Mountains Russia) revealed in a primary ecological succession. Ecology and Evolution 8:7401-7420. https://doi.org/10.1002/ece3.4258

Checinska Sielaff A, Upton RN, Hofmockel KS, Xu X, Polley HW, Wilsey BJ. 2018. Microbial community structure and functions differ between native and novel (exotic-dominated) grassland ecosystems in an 8-year experiment. Plant and Soil 432:359-372. https://doi.org/10.1007/s11104-018-3796-1

Chen W, Hambleton S, Seifert KA, Carisse O, Diarra MS, Peters RD, Lowe C, Chapados JT, Lévesque CA. 2018. Assessing performance of spore samplers in monitoring aeromycobiota and fungal plant pathogen diversity in Canada. Applied and Environmental Microbiology 84:e02601-17. https://doi.org/10.1128/AEM.02601-17

Chen W, Xu R, Wu Y, Chen J, Zhang Y, Hu T, Yuan X, Zhou L, Tan T, Fan J. 2018. Plant diversity is coupled with beta not alpha diversity of soil fungal communities following N enrichment in a semi-arid grassland. Soil Biology and Biochemistry 116:388-398. https://doi.org/10.1016/j.soilbio.2017.10.039

Cline LC, Hobbie SE, Madritch MD, Buyarski CR, Tilman D, Cavender-Bares JM. 2018. Resource availability underlies the plant-fungal diversity relationship in a grassland ecosystem. Ecology 99:204-216. https://doi.org/10.1002/ecy.2075

Cline LC, Huggins JA, Hobbie SE, Kennedy P.G. 2018. Organic nitrogen addition suppresses fungal richness and alters community composition in temperate forest soils. Soil Biology and Biochemistry 125:222-230. https://doi.org/10.1016/j.soilbio.2018.07.008

Cline LC, Schilling JS, Menke J, Groenhof E, Kennedy PG. 2018. Ecological and functional effects of fungal endophytes on wood decomposition. Functional Ecology 32:181-191. https://doi.org/10.1111/1365-2435.12949

Coleine C, Zucconi L, Onofri S, Pombubpa N, Stajich JE, Selbmann L. 2018. Sun exposure shapes functional grouping of fungi in cryptoendolithic antarctic communities. Life 8:e19. https://doi.org/10.3390/life8020019

Corrales A, Henkel TW, Smith ME. 2018. Ectomycorrhizal associations in the tropics – biogeography diversity patterns and ecosystem roles. New Phytologist 220:1076-1091. https://doi.org/10.1111/nph.15151

Courty PE, Buée M, Tech JJT, Brulé D, Colin Y, Leveau JHJ, Uroz S. 2018. Impact of soil pedogenesis on the diversity and composition of fungal communities across the California soil chronosequence of Mendocino. Mycorrhiza 28:343-356. https://doi.org/10.1007/s00572-018-0829-9

Cregger MA, Veach AM, Yang ZK, Crouch MJ, Vilgalys R, Tuskan GA, Schadt CW. 2018. The <i>Populus</i> holobiont: Dissecting the effects of plant niches and genotype on the microbiome. Microbiome 6e:31. https://doi.org/10.1186/s40168-018-0413-8

Dai Z, Enders A, Rodrigues JLM, Hanley KL, Brookes PC, Xu J, Lehmann J. 2018. Soil fungal taxonomic and functional community composition as affected by biochar properties. Soil Biology and Biochemistry 126:159-167. https://doi.org/10.1016/j.soilbio.2018.09.001

Dang P, Vu NH, Shen Z, Liu J, Zhao F, Zhu H, Yu X, Zhao Z. 2018. Changes in soil fungal communities and vegetation following afforestation with Pinus tabulaeformis on the Loess Plateau. Ecosphere 9:e02401. https://doi.org/10.1002/ecs2.2401

Delelegn YT, Purahong W, Sandén H, Yitaferu B, Godbold DL, Wubet T. 2018. Transition of Ethiopian highland forests to agriculture-dominated landscapes shifts the soil microbial community composition. BMC Ecology 18:e58. https://doi.org/10.1186/s12898-018-0214-8

Delgado-Baquerizo M, Eldridge DJ, Travers SK, Val J, Oliver I, Bissett A. 2018. Effects of climate legacies on above- and below-ground community assembly. Global Change Biology 24:4330-4339. https://doi.org/10.1111/gcb.14306

Delgado-Baquerizo M, Reith F, Dennis PG, Hamonts K, Powell JR, Young A, Singh BK, Bissett A. 2018. Ecological drivers of soil microbial diversity and soil biological networks in the Southern Hemisphere. Ecology 99:583-596. https://doi.org/10.1002/ecy.2137

Derocles SAP, Bohan DA, Dumbrell AJ, Kitson JJN, Massol F, Pauvert C, Plantegenest M, Vacher C, Evans DM. 2018. Biomonitoring for the 21st century: Integrating next-generation sequencing into ecological network analysis. Advances in Ecological Research 58:1-62. https://doi.org/10.1016/bs.aecr.2017.12.001

Detheridge AP, Comont D, Callaghan TM, Bussell J, Brand G, Gwynn-Jones D, Scullion J, Griffith GW. 2018. Vegetation and edaphic factors influence rapid establishment of distinct fungal communities on former coal-spoil sites. Fungal Ecology 33:92-103. https://doi.org/10.1016/j.funeco.2018.02.002

Dissanayake AJ, Purahong W, Wubet T, Hyde KD, Zhang W, Xu H, Zhang G, Fu C, Liu M, Xing Q, Li X, Yan J. 2018. Direct comparison of culture-dependent and culture-independent molecular approaches reveal the diversity of fungal endophytic communities in stems of grapevine (<i>Vitis vinifera</i>). Fungal Diversity 90:85-107. https://doi.org/10.1007/s13225-018-0399-3

Dundas SJ, Hopkins AJM, Ruthrof KX, Tay NE, Burgess TI, Hardy GESJ, Fleming PA. 2018. Digging mammals contribute to rhizosphere fungal community composition and seedling growth. Biodiversity and Conservation 27:3071-3086. https://doi.org/10.1007/s10531-018-1575-1

Eduardo N, Florencia S, Nicolás P, József G. 2018. Richness species composition and functional groups in Agaricomycetes communities along a vegetation and elevational gradient in the Andean Yungas of Argentina. Biodiversity and Conservation 27:1849-1871. https://doi.org/10.1007/s10531-018-1512-3

Egidi E, May TW, Franks AE. 2018. Seeking the needle in the haystack: Undetectability of mycorrhizal fungi outside of the plant rhizosphere associated with an endangered Australian orchid. Fungal Ecology 33:13-23. https://doi.org/10.1016/j.funeco.2018.01.002

Eldridge DJ, Delgado-Baquerizo M. 2018. Functional groups of soil fungi decline under grazing. Plant and Soil 426:51-60. https://doi.org/10.1007/s11104-018-3617-6

Erlandson S. Wei X. Savage J. Cavender-Bares J. Peay K. 2018. Soil abiotic variables are more important than Salicaceae phylogeny or habitat specialization in determining soil microbial community structure. Molecular Ecology 27:2007-2024. https://doi.org/10.1111/mec.14576

Fernandez CW, Kennedy PG. 2018. Melanization of mycorrhizal fungal necromass structures microbial decomposer communities. Journal of Ecology 106:468-479. https://doi.org/10.1111/1365-2745.12920

Frac M, Hannula SE, Belka M, Jȩdryczka M. 2018. Fungal biodiversity and their role in soil health. Frontiers in Microbiology 9:e707. https://doi.org/10.3389/fmicb.2018.00707

Gallart M, Adair KL, Love J, Meason DF, Clinton PW, Xue J, Turnbull MH. 2018. Host genotype and nitrogen form shape the root microbiome of <i>Pinus radiata</i>. Microbial Ecology 75:419-433. https://doi.org/10.1007/s00248-017-1055-2

Garzoli L, Poli A, Prigione V, Gnavi G, Varese GC. 2018. Peacock's tail with a fungal cocktail: First assessment of the mycobiota associated with the brown alga <i>Padina pavonica</i>. Fungal Ecology 35:87-97. https://doi.org/10.1016/j.funeco.2018.05.005

Ghobad-Nejhad M, Meyn R, Langer E. 2018. Endophytic fungi isolated from healthy and declining persian oak (<i>Quercus brantii</i>) in western Iran. Nova Hedwigia 107:273-290. https://doi.org/10.1127/nova_hedwigia/2018/0470

Gluck-Thaler E, Slot JC. 2018. Specialized plant biochemistry drives gene clustering in fungi. ISME Journal 12:1694-1705. https://doi.org/10.1038/s41396-018-0075-3

Haelewaters D, Dirks AC, Kappler LA, Mitchell JK, Quijada L, Vandegrift R, Buyck B, Pfister DH. 2018. A preliminary checklist of fungi at the Boston Harbor Islands. Northeastern Naturalist 25:45-76. https://doi.org/10.1656/045.025.s904

Hahn PG, Bullington L, Larkin B, LaFlamme K, Maron JL, Lekberg Y. 2018. Effects of short- and long-term variation in resource conditions on soil fungal communities and plant responses to soil biota. Frontiers in Plant Science 871:e1605. https://doi.org/10.3389/fpls.2018.01605

Hargreaves J, Brickle P, van West P. 2018. The fungal ecology of seabird nesting sites in the Falkland Islands indicates a niche for mycoparasites. Fungal Ecology 36:99-108. https://doi.org/10.1016/j.funeco.2018.08.005

Harrison JG, Philbin CS, Gompert Z, Forister GW, Hernandez-Espinoza L, Sullivan BW, Wallace IS, Beltran L, Dodson CD, Francis JS, Schlageter A, Shelef O, Yoon SA, Forister ML. 2018. Deconstruction of a plant-arthropod community reveals influential plant traits with nonlinear effects on arthropod assemblages. Functional Ecology 32:1317-1328. https://doi.org/10.1111/1365-2435.13060

Hopkins AJM, Ruthrof KX, Fontaine JB, Matusick G, Dundas SJ, Hardy GE. 2018. Forest die-off following global-change-type drought alters rhizosphere fungal communities. Environmental Research Letters 13:e095006. https://doi.org/10.1088/1748-9326/aadc19

Hu W, Strom N, Haarith D, Chen S, Bushley KE. 2018. Mycobiome of cysts of the soybean cyst nematode under long term crop rotation. Frontiers in Microbiology 9:e386. https://doi.org/10.3389/fmicb.2018.00386

Hui N, Liu X, Jumpponen A, Setälä H, Kotze DJ, Biktasheva L, Romantschuk M. 2018. Over twenty years farmland reforestation decreases fungal diversity of soils but stimulates the return of ectomycorrhizal fungal communities. Plant and Soil 427:231-244. https://doi.org/10.1007/s11104-018-3647-0

Jacobsen RM, Sverdrup-Thygeson A, Kauserud H, Birkemoe T. 2018. Revealing hidden insect-fungus interactions; moderately specialized modular and anti-nested detritivore networks. Proceedings of the Royal Society B: Biological Sciences 285:e20172833. https://doi.org/10.1098/rspb.2017.2833

Jacobsen RM, Sverdrup-Thygeson A, Kauserud H, Mundra S, Birkemoe T. 2018. Exclusion of invertebrates influences saprotrophic fungal community and wood decay rate in an experimental field study. Functional Ecology 32:2571-2582. https://doi.org/10.1111/1365-2435.13196

Janoušková M, Kohout P, Moradi J, Doubková P, Frouz J, Vosolsobě S, Rydlová J. 2018. Microarthropods influence the composition of rhizospheric fungal communities by stimulating specific taxa. Soil Biology and Biochemistry 122:120-130. https://doi.org/10.1016/j.soilbio.2018.04.016

Jassey VEJ, Reczuga MK, Zielińska M, Słowińska S, Robroek BJM, Mariotte P, Seppey CVW, Lara E, Barabach J, Słowiński M, Bragazza L, Chojnicki BH, Lamentowicz M, Mitchell EAD, Buttler A. 2018. Tipping point in plant–fungal interactions under severe drought causes abrupt rise in peatland ecosystem respiration. Global Change Biology 24:972-986. https://doi.org/10.1111/gcb.13928

Jayawardena RS, Purahong W, Zhang W, Wubet T, Li XH, Liu M, Zhao W, Hyde KD, Liu JH, Yan J. 2018. Biodiversity of fungi on <i>Vitis vinifera</i> L. revealed by traditional and high-resolution culture-independent approaches. Fungal Diversity 90:1–84. https://doi.org/10.1007/s13225-018-0398-4

Kennedy PG, Mielke LA, Nguyen NH. 2018. Ecological responses to forest age habitat and host vary by mycorrhizal type in boreal peatlands. Mycorrhiza 28:315-328. https://doi.org/10.1007/s00572-018-0821-4

Kujala K, Mikkonen A, Saravesi K, Ronkanen A-K, Tiirola M. 2018. Microbial diversity along a gradient in peatlands treating mining-affected waters. FEMS Microbiology Ecology 94:fiy145. https://doi.org/10.1093/femsec/fiy145

LeBrun ES, Taylor DL, King RS, Back JA, Kang S. 2018. Rivers may constitute an overlooked avenue of dispersal for terrestrial fungi. Fungal Ecology 32:72-79. https://doi.org/10.1016/j.funeco.2017.12.003

Legrand F, Picot A, Cobo-Díaz JF, Carof M, Chen W, Le Floch G. 2018. Effect of tillage and static abiotic soil properties on microbial diversity. Applied Soil Ecology 132:135-145. https://doi.org/10.1016/j.apsoil.2018.08.016

Lekberg Y, Bever JD, Bunn RA, Callaway RM, Hart MM, Kivlin SN, Klironomos J, Larkin BG, Maron JL, Reinhart KO, Remke M, van der Putten WH. 2018. Relative importance of competition and plant–soil feedback their synergy context dependency and implications for coexistence. Ecology Letters 21:1268-1281. https://doi.org/10.1111/ele.13093

León-Sánchez L, Nicolás E, Goberna M, Prieto I, Maestre FT, Querejeta JI. 2018. Poor plant performance under simulated climate change is linked to mycorrhizal responses in a semi-arid shrubland. Journal of Ecology 106:960-976. https://doi.org/10.1111/1365-2745.12888

Li Q, Yan L, Ye L, Zhou J, Zhang B, Peng W, Zhang X, Li X. 2018. Chinese black truffle (<i>Tuber indicum</i>) alters the ectomycorrhizosphere and endoectomycosphere microbiome and metabolic profiles of the host tree <i>Quercus aliena</i>. Frontiers in Microbiology 9:e2202. https://doi.org/10.3389/fmicb.2018.02202

Li Q, Zhang B, Yang X, Ge Q. 2018. Deterioration-associated microbiome of stone monuments:Structure variation and assembly. Applied and Environmental Microbiology 84:e02680-17. https://doi.org/10.1128/AEM.02680-17

Liu S, Wang H, Deng Y, Tian P, Wang Q. 2018. Forest conversion induces seasonal variation in microbial β-diversity. Environmental Microbiology 20:111-123. https://doi.org/10.1111/1462-2920.14017

Looby CI, Treseder KK. 2018. Shifts in soil fungi and extracellular enzyme activity with simulated climate change in a tropical montane cloud forest. Soil Biology and Biochemistry 117:87-96. https://doi.org/10.1016/j.soilbio.2017.11.014

Lu X, He M, Ding J, Siemann E. 2018. Latitudinal variation in soil biota: Testing the biotic interaction hypothesis with an invasive plant and a native congener. ISME Journal 12:2811-2822. https://doi.org/10.1038/s41396-018-0219-5

Lumibao CY, Formel S, Elango V, Pardue JH, Blum M, Van Bael SA. 2018. Persisting responses of salt marsh fungal communities to the Deepwater Horizon oil spill. Science of the Total Environment 642:904-913. https://doi.org/10.1016/j.scitotenv.2018.06.077

Malacrinò A. 2018. Meta-Omics tools in the world of insect-microorganism interactions. Biology 7:e50. https://doi.org/10.3390/biology7040050

Malysheva EF, Malysheva VF, Shchepina ON, Novozhilov YK. 2018. Wildfire influence on structure and species composition of ectomycorrhizal fungal communities in pine forests in Northwest Russia: The results of metagenomic analysis. Mikologiya I Fitopatologiya 52:328-348. https://doi.org/10.1134/S0026364818050057

Mahnert A, Ortega RA, Berg C, Grube M, Berg G. 2018. Leaves of indoor ornamentals are biodiversity and functional hotspots for fungi. Frontiers in Microbiology 9:e2343. https://doi.org/10.3389/fmicb.2018.02343

Matsuoka S, Ogisu Y, Sakoh S, Hobara S, Osono T. 2018. Taxonomic functional and phylogenetic diversity of fungi along primary successional and elevational gradients near Mount Robson British Columbia. Polar Science. https://doi.org/10.1016/j.polar.2018.09.004

Maynard DS, Covey KR, Crowther TW, Sokol NW, Morrison EW, Frey SD, van Diepen LTA, Bradford MA. 2018. Species associations overwhelm abiotic conditions to dictate the structure and function of wood-decay fungal communities. Ecology 99:801-811. https://doi.org/10.1002/ecy.2165

Mello A, Balestrini R. 2018. Recent insights on biological and ecological aspects of ectomycorrhizal fungi and their interactions. Frontiers in Microbiology 9:e216. https://doi.org/10.3389/fmicb.2018.00216

Mommer L, Cotton TEA, Raaijmakers JM, Termorshuizen AJ, van Ruijven J, Hendriks M, van Rijssel SQ, van de Mortel JE, van der Paauw JW, Schijlen EGWM, Smit-Tiekstra AE, Berendse F, de Kroon H, Dumbrell AJ. 2018. Lost in diversity: The interactions between soil-borne fungi biodiversity and plant productivity. New Phytologist 218:542-553. https://doi.org/10.1111/nph.15036

Morrison EW, Pringle A, van Diepen LTA, Frey SD. 2018. Simulated nitrogen deposition favors stress-tolerant fungi with low potential for decomposition. Soil Biology and Biochemistry 125:75-85. https://doi.org/10.1016/j.soilbio.2018.06.027

Mushinski RM, Gentry TJ, Boutton TW. 2018. Organic matter removal associated with forest harvest leads to decade scale alterations in soil fungal communities and functional guilds. Soil Biology and Biochemistry 127:127-136. https://doi.org/10.1016/j.soilbio.2018.09.019

Nagati M, Roy M, Manzi S, Richard F, Desrochers A, Gardes M, Bergeron Y. 2018. Impact of local forest composition on soil fungal communities in a mixed boreal forest. Plant and Soil 432:345-357. https://doi.org/10.1007/s11104-018-3806-3

Nawaz A, Purahong W, Lehmann R, Herrmann M, Totsche KU, Küsel K, Wubet T, Buscot F. 2018. First insights into the living groundwater mycobiome of the terrestrial biogeosphere. Water Research 145:50-61. https://doi.org/10.1016/j.watres.2018.07.067

Ni Y, Yang T, Zhang K, Shen C, Chu H. 2018. Fungal communities along a small-scale elevational gradient in an alpine tundra are determined by soil carbon nitrogen ratios. Frontiers in Microbiology 9:e1815. https://doi.org/10.3389/fmicb.2018.01815

Nie S, Lei X, Zhao L, Brookes PC, Wang F, Chen C, Yang W, Xing S. 2018. Fungal communities and functions response to long-term fertilization in paddy soils. Applied Soil Ecology 130:251-258. https://doi.org/10.1016/j.apsoil.2018.06.008

Nie S-A, Wang Y, Lei X-M, Zhao L-X, Lin R-Y, Wang F, Xing S-H. 2018. Responses of fungal community structure and functional group to fertilization in yellow clayey soil. Chinese Journal of Applied Ecology 29:2721-2729. https://doi.org/10.13287/j.1001-9332.201808.003

Niu Y, Bainard LD, May WE, Hossain Z, Hamel C, Gan Y. 2108. Intensified pulse rotations buildup pea rhizosphere pathogens in cereal and pulse based cropping systems. Frontiers in Microbiology 9:e1909. https://doi.org/10.3389/fmicb.2018.01909

Oh S-Y, Cho HJ, Eimes JA, Han S-K, Kim CS, Lim YW. 2018. Guild patterns of basidiomycetes community associated with <i>Quercus mongolica</i> in Mt. Jeombong Republic of Korea. Mycobiology 46:13-23. https://doi.org/10.1080/12298093.2018.1454009

Ohlmann M, Mazel F, Chalmandrier L, Bec S, Coissac E, Gielly L, Pansu J, Schilling V, Taberlet P, Zinger L, Chave J, Thuiller W. 2018. Mapping the imprint of biotic interactions on β-diversity. Ecology Letters 21:1660-1669. https://doi.org/10.1111/ele.13143

Osborne OG, De-Kayne R, Bidartondo MI, Hutton I, Baker WJ, Turnbull CGN, Savolainen V. 2018. Arbuscular mycorrhizal fungi promote coexistence and niche divergence of sympatric palm species on a remote oceanic island. New Phytologist 217:1254-1266. https://doi.org/10.1111/nph.14850

Otsing E, Barantal S, Anslan S, Koricheva J, Tedersoo L. 2018. Litter species richness and composition effects on fungal richness and community structure in decomposing foliar and root litter. Soil Biology and Biochemistry 125:328-339. https://doi.org/10.1016/j.soilbio.2018.08.006

Palmer JM, Jusino MA, Banik MT, Lindner DL. 2018. Non-biological synthetic spike-in controls and the AMPtk software pipeline improve mycobiome data. PeerJ 2018:e4925. https://doi.org/10.7717/peerj.4925

Pfennigwerth AA, Van Nuland ME, Bailey JK, Schweitzer JA. 2018. Plant–soil feedbacks mediate shrub expansion in declining forests but only in the right light. Journal of Ecology 106:179-194. https://doi.org/10.1111/1365-2745.12833

Peršoh D, Stolle N, Brachmann A, Begerow D, Rambold G. 2018. Fungal guilds are evenly distributed along a vertical spruce forest soil profile while individual fungi show pronounced niche partitioning. Mycological Progress 17:925-939. https://doi.org/10.1007/s11557-018-1405-6

Philpott TJ, Barker JS, Prescott CE, Grayston SJ. 2018. Limited effects of variable-retention harvesting on fungal communities decomposing fine roots in coastal temperate rainforests. Applied and Environmental Microbiology 84:e02061-17. https://doi.org/10.1128/AEM.02061-17

Porter TM, Hajibabaei M. 2018. Scaling up: A guide to high-throughput genomic approaches for biodiversity analysis. Molecular Ecology 27:313-338. https://doi.org/10.1111/mec.14478

Qian X, Chen L, Guo X, He D, Shi M, Zhang D. 2018. Shifts in community composition and co-occurrence patterns of phyllosphere fungi inhabiting <i>Mussaenda shikokiana</i> along an elevation gradient. PeerJ 2018:e5767. https://doi.org/10.7717/peerj.5767

Ramirez KS, Geisen S, Morriën E, Snoek BL, van der Putten WH. 2018. Network analyses can advance above-below-ground ecology. Trends in Plant Science 23:759-768. https://doi.org/10.1016/j.tplants.2018.06.009

Roy J, Bonneville J-M, Saccone P, Ibanez S, Albert CH, Boleda M, Gueguen M, Ohlmann M, Rioux D, Clément J-C, Lavergne S, Geremia RA. 2018. Differences in the fungal communities nursed by two genetic groups of the alpine cushion plant <i>Silene acaulis</i>. Ecology and Evolution 8:11568-11581. https://doi.org/10.1002/ece3.4606

Santalahti M, Sun H, Sietiö O-M, Köster K, Berninger F, Laurila T, Pumpanen J, Heinonsalo J. 2018. Reindeer grazing alter soil fungal community structure and litter decomposition related enzyme activities in boreal coniferous forests in Finnish Lapland. Applied Soil Ecology 132:74-82. https://doi.org/10.1016/j.apsoil.2018.08.013

Schlatter DC, Kahl K, Carlson B, Huggins DR, Paulitz T. 2018. Fungal community composition and diversity vary with soil depth and landscape position in a no-till wheat-based cropping system. FEMS Microbiology Ecology 94:fiy098. https://doi.org/10.1093/femsec/fiy098

Schön ME, Nieselt K, Garnica S. 2018. Belowground fungal community diversity and composition associated with Norway spruce along an altitudinal gradient. PLoS ONE 13:e0208493. https://doi.org/10.1371/journal.pone.0208493

Schöps R, Goldmann K, Herz K, Lentendu G, Schöning I, Bruelheide H, Wubet T, Buscot F. 2018. Land-use intensity rather than plant functional identity shapes bacterial and fungal rhizosphere communities. Frontiers in Microbiology 9:e2711. https://doi.org/10.3389/fmicb.2018.02711

Schroeder JW, Martin JT, Angulo DF, Barbosa JM, Perea R, Arias-Del Razo I, Sebastián-González E, Dirzo R. 2018. Community composition and diversity of Neotropical root-associated fungi in common and rare trees. Biotropica 50:694-703. https://doi.org/10.1111/btp.12553

Seibold S, Cadotte MW, MacIvor JS, Thorn S, Müller J. 2018. The Necessity of multitrophic approaches in community ecology. Trends in Ecology and Evolution 33:754-764. https://doi.org/10.1016/j.tree.2018.07.001

Semchenko M, Leff JW, Lozano YM, Saar S, Davison J, Wilkinson A, Jackson BG, Pritchard WJ, De Long JR, Oakley S, Mason KE, Ostle NJ, Baggs EM, Johnson D, Fierer N, Bardgett RD. 2018. Fungal diversity regulates plant-soil feedbacks in temperate grassland. Science Advances 4:eaau4578. https://doi.org/10.1126/sciadv.aau4578

Shi LL, Wen Y, Yang ZJ, Zang HD, Gui H, Zou XM, Mortimer P. 2018. Dominant tree species identity effects on soil fungi are context dependent. Mycosphere 9:790-802. https://doi.org/10.5943/mycosphere/9/4/7

Siriyappagouder P, Kiron V, Lokesh J, Rajeish M, Kopp M, Fernandes J. 2018. The intestinal mycobiota in wild zebrafish comprises mainly Dothideomycetes while Saccharomycetes predominate in their laboratory-reared counterparts. Frontiers in Microbiology 9:e387. https://doi.org/10.3389/fmicb.2018.00387

Taberlet P, Bonin A, Zinger L, Coissac E. 2018. Environmental DNA: For biodiversity research and monitoring. In: Taberlet P, Bonin A, Zinger L, Coissac E (eds.) Environmental DNA: For Biodiversity Research and Monitoring. Oxford Scholarship Online pp. 1-253. https://doi.org/10.1093/oso/9780198767220.001.0001

Taudière A, Bellanger J-M, Carcaillet C, Hugot L, Kjellberg F, Lecanda A, Lesne A, Moreau P-A, Scharmann K, Leidel S, Richard F. 2018. Diversity of foliar endophytic ascomycetes in the endemic Corsican pine forests. Fungal Ecology 36:128-140. https://doi.org/10.1016/j.funeco.2018.07.008

Tedersoo L, Sánchez-Ramírez S, Kõljalg U, Bahram M, Döring M, Schigel D, May T, Ryberg M, Abarenkov K. 2018. High-level classification of the Fungi and a tool for evolutionary ecological analyses. Fungal Diversity 90:135-159. https://doi.org/10.1007/s13225-018-0401-0

Toju H, Peay KG, Yamamichi M, Narisawa K, Hiruma K, Naito K, Fukuda S, Ushio M, Nakaoka S, Onoda Y, Yoshida K, Schlaeppi K, Bai Y, Sugiura R, Ichihashi Y, Minamisawa K, Kiers ET. 2018. Core microbiomes for sustainable agroecosystems. Nature Plants 4:247-257. https://doi.org/10.1038/s41477-018-0139-4

Toju H, Sato H. 2018. Root-associated fungi shared between arbuscular mycorrhizal and ectomycorrhizal conifers in a temperate forest. Frontiers in Microbiology 9:e433. https://doi.org/10.3389/fmicb.2018.00433

Toju H, Sato H, Yamamoto S, Tanabe AS. 2018. Structural diversity across arbuscular mycorrhizal ectomycorrhizal and endophytic plant-fungus networks. BMC Plant Biology 18:e292. https://doi.org/10.1186/s12870-018-1500-5

Toju H, Tanabe AS, Sato H. 2018. Network hubs in root-associated fungal metacommunities. Microbiome 6:e116. https://doi.org/10.1186/s40168-018-0497-1

Toole DR, Cannon GH, Brislawn CJ, Graves JM, Lamendella R, Muth TR, Muth NZ. 2018. Differences in soil fungal assemblages associated with native and non-native tree species of varying weediness. Biological Invasions 20:891-904. https://doi.org/10.1007/s10530-017-1580-4

Urbina H, Breed MF, Zhao W, Lakshmi Gurrala K, Andersson SGE, Ågren J, Baldauf S, Rosling A. 2018. Specificity in <i>Arabidopsis thaliana</i> recruitment of root fungal communities from soil and rhizosphere. Fungal Biology 122:231-240. https://doi.org/10.1016/j.funbio.2017.12.013

van Agtmaal M, Straathof AL, Termorshuizen A, Lievens B, Hoffland E, de Boer W. 2018, Volatile-mediated suppression of plant pathogens is related to soil properties and microbial community composition. Soil Biology and Biochemistry 117:164-174. https://doi.org/10.1016/j.soilbio.2017.11.015

Veach AM, Stokes CE, Knoepp J, Jumpponen A, Baird R. 2018. Fungal Communities and functional guilds shift along an elevational gradient in the southern Appalachian Mountains. Microbial Ecology 76:156-168. https://doi.org/10.1007/s00248-017-1116-6

Vowles T, Lindwall F, Ekblad A, Bahram M, Furneaux BR, Ryberg M, Björk RG. 2018. Complex effects of mammalian grazing on extramatrical mycelial biomass in the Scandes forest-tundra ecotone. Ecology and Evolution 8:1019-1030. https://doi.org/10.1002/ece3.3657

Walker DM, Murray CM, Talbert D, Tinker P, Graham SP, Crowther TW. 2018. A salamander's top down effect on fungal communities in a detritivore ecosystem. FEMS Microbiology Ecology 94:fiy168. https://doi.org/10.1093/femsec/fiy168

Wang J, Chen C, Ye Z, Li J, Feng Y, Lu Q. 2018. Relationships between fungal and plant communities differ between desert and grassland in a typical dryland region of northwest China. Frontiers in Microbiology 9:e2327. https://doi.org/10.3389/fmicb.2018.02327

Wang J, Rhodes G, Huang Q, Shen Q. 2018. Plant growth stages and fertilization regimes drive soil fungal community compositions in a wheat-rice rotation system. Biology and Fertility of Soils 54:731-742. https://doi.org/10.1007/s00374-018-1295-4

Wang K, Mao H, Li X. 2018. Functional characteristics and influence factors of microbial community in sewage sludge composting with inorganic bulking agent. Bioresource Technology 249:527-535. https://doi.org/10.1016/j.biortech.2017.10.034

Wang K, Yin X, Mao H, Chu C, Tian Y. 2018. Changes in structure and function of fungal community in cow manure composting. Bioresource Technology 255:123-130. https://doi.org/10.1016/j.biortech.2018.01.064

Wei Z, Liu Y, Feng K, Li S, Wang S, Jin D, Zhang Y, Chen H, Yin H, Xu M, Deng Y. 2018. The divergence between fungal and bacterial communities in seasonal and spatial variations of wastewater treatment plants. Science of the Total Environment 628-629:969-978. https://doi.org/10.1016/j.scitotenv.2018.02.003

Weißbecker C, Wubet T, Lentendu G, Kühn P, Scholten T, Bruelheide H, Buscot F. 2018. Experimental evidence of functional group-dependent effects of tree diversity on soil fungi in subtropical forests. Frontiers in Microbiology 9:e2312. https://doi.org/10.3389/fmicb.2018.02312

Whalen ED, Smith RG, Grandy AS, Frey SD. 2018. Manganese limitation as a mechanism for reduced decomposition in soils under atmospheric nitrogen deposition. Soil Biology and Biochemistry 127:252-263. https://doi.org/10.1016/j.soilbio.2018.09.025

Whitman T, Neurath R, Perera A, Chu-Jacoby I, Ning D, Zhou J, Nico P, Pett-Ridge J, Firestone M. 2018. Microbial community assembly differs across minerals in a rhizosphere microcosm. Environmental Microbiology 20:4444-4460. https://doi.org/10.1111/1462-2920.14366

Xu W, Gong L-F, Pang K-L, Luo Z-H. 2018. Fungal diversity in deep-sea sediments of a hydrothermal vent system in the Southwest Indian Ridge. Deep-Sea Research Part I: Oceanographic Research Papers 131:16-26. https://doi.org/10.1016/j.dsr.2017.11.001

Yan D, Mills JG, Gellie NJC, Bissett A, Lowe AJ, Breed MF. 2018. High-throughput eDNA monitoring of fungi to track functional recovery in ecological restoration. Biological Conservation 217:113-120. https://doi.org/10.1016/j.biocon.2017.10.035

Yang H, Zhao X, Liu C, Bai L, Zhao M, Li L. 2018. Diversity and characteristics of colonization of root-associated fungi of <i>Vaccinium uliginosum</i>. Scientific Reports 8:e15283. https://doi.org/10.1038/s41598-018-33634-1

Yu Z, Li Y, Hu X, Jin J, Wang G, Tang C, Liu J, Liu X, Franks A, Egidi E, Xie Z. 2018. Elevated CO2 increases the abundance but simplifies networks of soybean rhizosphere fungal community in Mollisol soils. Agriculture Ecosystems and Environment 264:94-98. https://doi.org/10.1016/j.agee.2018.05.006

Zhang J, Zhang B, Liu Y, Guo Y, Shi P, Wei G. 2018. Distinct large-scale biogeographic patterns of fungal communities in bulk soil and soybean rhizosphere in China. Science of the Total Environment 644:791-800. https://doi.org/10.1016/j.scitotenv.2018.07.016


<b>2017</b>

Anthony MA, Frey SD, Stinson KA. 2017. Fungal community homogenization shift in dominant trophic guild and appearance of novel taxa with biotic invasion. Ecosphere 8:e01951. https://doi.org/10.1002/ecs2.1951

Asemaninejad A, Thorn RG, Lindo Z. 2017. Vertical distribution of fungi in hollows and hummocks of boreal peatlands. Fungal Ecology 27:59-68. https://doi.org/10.1016/j.funeco.2017.02.002

Bárta J, Tahovská K, Šantrůčková H, Oulehle F. 2017. Microbial communities with distinct denitrification potential in spruce and beech soils differing in nitrate leaching. Scientific Reports 7:e9738. https://doi.org/10.1038/s41598-017-08554-1

Bainard LD, Navarro-Borrell A, Hamel C, Braun K, Hanson K, Gan Y. 2017. Increasing the frequency of pulses in crop rotations reduces soil fungal diversity and increases the proportion of fungal pathotrophs in a semiarid agroecosystem. Agriculture Ecosystems and Environment 240:206-214. https://doi.org/10.1016/j.agee.2017.02.020

Benitez M-S, Osborne SL, Lehman RM. 2017. Previous crop and rotation history effects on maize seedling health and associated rhizosphere microbiome. Scientific Reports 7:e15709. https://doi.org/10.1038/s41598-017-15955-9

Brunner I, Frey B, Hartmann M, Zimmermann S, Graf F, Suz LM, Niskanen T, Bidartondo MI, Senn-Irlet B. 2017. Ecology of alpine macrofungi: Combining historical with recent data. Frontiers in Microbiology 8:e2066. https://doi.org/10.3389/fmicb.2017.02066

Cho H, Kim M, Tripathi B, Adams J. 2017. Changes in soil fungal community structure with increasing disturbance frequency. Microbial Ecology 74:62-77. https://doi.org/10.1007/s00248-016-0919-1

Djemiel C, Grec S, Hawkins S. 2017. Characterization of bacterial and fungal community dynamics by high-throughput sequencing (HTS) metabarcoding during flax dew-retting. Frontiers in Microbiology 8:e2052. https://doi.org/10.3389/fmicb.2017.02052

Durand A, Maillard F, Foulon J, Gweon HS, Valot B, Chalot M. 2017. Environmental metabarcoding reveals contrasting belowground and aboveground fungal communities from poplar at a Hg phytomanagement site. Microbial Ecology 74:795-809. https://doi.org/10.1007/s00248-017-0984-0

Eisenhauer N, Antunes PM, Bennett AE, Birkhofer K, Bissett A, Bowker MA, Caruso T, Chen B, Coleman DC, Boer WD, Ruiter PD, DeLuca TH, Frati F, Griffiths BS, Hart MM, Hättenschwiler S, Haimi J, Heethoff M, Kaneko N, Kelly LC, Leinaas HP, Lindo Z, Macdonald C, Rillig MC, Ruess L, Scheu S, Schmidt O, Seastedt TR, Straalen NMV, Tiunov AV, Zimmer M, Powell JR. Priorities for research in soil ecology. Pedobiologia 63:1-7. https://doi.org/10.1016/j.pedobi.2017.05.003

Epp Schmidt DJ, Pouyat R, Szlavecz K, Setälä H, Kotze DJ, Yesilonis I, Cilliers S, Hornung E, Dombos M, Yarwood SA. 2017. Urbanization erodes ectomycorrhizal fungal diversity and may cause microbial communities to converge. Nature Ecology and Evolution 1:e0123. https://doi.org/10.1038/s41559-017-0123

Fernandez CW, Nguyen NH, Stefanski A, Han Y, Hobbie SE, Montgomery RA, Reich PB, Kennedy PG. 2017. Ectomycorrhizal fungal response to warming is linked to poor host performance at the boreal-temperate ecotone. Global Change Biology 23:1598-1609. https://doi.org/10.1111/gcb.13510

Fukasawa Y, Ando Y, Song Z. 2017. Comparison of fungal communities associated with spruce seedling roots and bryophyte carpets on logs in an old-growth subalpine coniferous forest in Japan. Fungal Ecology 30:122-131. https://doi.org/10.1016/j.funeco.2017.10.001

Geisen S, Kostenko O, Cnossen MC, ten Hooven FC, Vreš B, van der Putten WH. 2017. Seed and root endophytic fungi in a range expanding and a related plant species. Frontiers in Microbiology 8:e1645. https://doi.org/10.3389/fmicb.2017.01645

Gibbons SM, Lekberg Y, Mummey DL, Sangwan N, Ramsey PW, Gilbert JA. 2017. Invasive plants rapidly reshape soil properties in a grassland ecosystem. mSystems 2:e00178. https://doi.org/10.1128/mSystems.00178-16

Grau O, Geml J, Pérez-Haase A, Ninot JM, Semenova-Nelsen TA, Peñuelas J. 2017. Abrupt changes in the composition and function of fungal communities along an environmental gradient in the high Arctic. Molecular Ecology 26:4798-4810. https://doi.org/10.1111/mec.14227

Grilli G, Longo S, Huais PY, Pereyra M, Verga EG, Urcelay C, Galetto L. 2017. Fungal diversity at fragmented landscapes:synthesis and future perspectives. Current Opinion in Microbiology 37:161-165. https://doi.org/10.1016/j.mib.2017.09.003

Grilli G, Longo S, Huais PY, Pereyra M, Verga E, Urcelay C, Galetto L. 2017. Fungal diversity is negatively affected by habitat fragmentation:a meta-analysis. Current Opinion in Microbiology 37:61-66. https://doi.org/10.1016/j.mib.2017.03.015

Hagh Doust N, Akbarinia M, Safaie N, Yousefzadeh H, Bálint M. 2017. Community analysis of Persian oak fungal microbiome under dust storm conditions. Fungal Ecology 29:1-9. https://doi.org/10.1016/j.funeco.2017.05.002

Hannula SE, Morriën E, De Hollander M, Van Der Putten WH, Van Veen JA, De Boer W. 2017. Shifts in rhizosphere fungal community during secondary succession following abandonment from agriculture. ISME Journal 11:2294-2304. https://doi.org/10.1038/ismej.2017.90

Hartmann M, Brunner I, Hagedorn F, Bardgett RD, Stierli B, Herzog C, Chen X, Zingg A, Graf-Pannatier E, Rigling A, Frey B. 2017. A decade of irrigation transforms the soil microbiome of a semi-arid pine forest. Molecular Ecology 26:1190-1206. https://doi.org/10.1111/mec.13995

He D, Shen W, Eberwein J, Zhao Q, Ren L, Wu QL. 2017. Diversity and co-occurrence network of soil fungi are more responsive than those of bacteria to shifts in precipitation seasonality in a subtropical forest. Soil Biology and Biochemistry 115:499-510. https://doi.org/10.1016/j.soilbio.2017.09.023

He J, Tedersoo L, Hu A, Han C, He D, Wei H, Jiao M, Anslan S, Nie Y, Jia Y, Zhang G, Yu G, Liu S, Shen W. 2017. Greater diversity of soil fungal communities and distinguishable seasonal variation in temperate deciduous forests compared with subtropical evergreen forests of eastern China. FEMS Microbiology Ecology 93:fix069. https://doi.org/10.1093/femsec/fix069

Hiiesalu I, Bahram M, Tedersoo L. 2017. Plant species richness and productivity determine the diversity of soil fungal guilds in temperate coniferous forest and bog habitats. Molecular Ecology 26:4846-4858. https://doi.org/10.1111/mec.14246

Hui N, Jumpponen A, Francini G, Kotze DJ, Liu X, Romantschuk M, Strömmer R, Setälä H. 2017. Soil microbial communities are shaped by vegetation type and park age in cities under cold climate. Environmental Microbiology 19:1281-1295. https://doi.org/10.1111/1462-2920.13660

Hui N, Liu X, Johan Kotze D, Jumpponen A, Francini G, Setälä H. 2017. Ectomycorrhizal fungal communities in urban parks are similar to those in natural forests but shaped by vegetation and park age. Applied and Environmental Microbiology 83:e01797-17. https://doi.org/10.1128/AEM.01797-17

Jacobsen RM, Kauserud H, Sverdrup-Thygeson A, Bjorbækmo MM, Birkemoe T. 2017. Wood-inhabiting insects can function as targeted vectors for decomposer fungi. Fungal Ecology 29:76-84. https://doi.org/10.1016/j.funeco.2017.06.006

Kamutando CN, Vikram S, Kamgan-Nkuekam G, Makhalanyane TP, Greve M, Roux JJL, Richardson DM, Cowan D, Valverde A. 2017. Soil nutritional status and biogeography influence rhizosphere microbial communities associated with the invasive tree <i>Acacia dealbata</i>. Scientific Reports 7:e6472. https://doi.org/10.1038/s41598-017-07018-w

Keymer DP, Lankau RA. 2017. Disruption of plant–soil–microbial relationships influences plant growth. Journal of Ecology 105:816-827. https://doi.org/10.1111/1365-2745.12716

Kirker GT, Bishell AB, Jusino MA, Palmer JM, Hickey WJ, Lindner DL. 2018. Amplicon-based sequencing of soil fungi from wood preservative test sites. Frontiers in Microbiology 8:e1997. https://doi.org/10.3389/fmicb.2017.01997

Kolaříková Z, Kohout P, Krüger C, Janoušková M, Mrnka L, Rydlová J. 2017. Root-associated fungal communities along a primary succession on a mine spoil:Distinct ecological guilds assemble differently. Soil Biology and Biochemistry 113:143-152. https://doi.org/10.1016/j.soilbio.2017.06.004

Knoblochová T, Kohout P, Püschel D, Doubková P, Frouz J, Cajthaml T, Kukla J, Vosátka M, Rydlová J. 2017. Asymmetric response of root-associated fungal communities of an arbuscular mycorrhizal grass and an ectomycorrhizal tree to their coexistence in primary succession. Mycorrhiza 27:775-789. https://doi.org/10.1007/s00572-017-0792-x

Lawrence KL, Wise DH. 2017. Long-term resource addition to a detrital food web yields a pattern of responses more complex than pervasive bottom-up control. PeerJ 2017:e3572. https://doi.org/10.7717/peerj.3572

Leff JW, Lynch RC, Kane NC, Fierer N. 2017. Plant domestication and the assembly of bacterial and fungal communities associated with strains of the common sunflower <i>Helianthus annuus</i>. New Phytologist 214:412-423. https://doi.org/10.1111/nph.14323

McGee CF, Byrne H, Irvine A, Wilson J. 2017. Diversity and dynamics of the DNA-and cDNA-derived compost fungal communities throughout the commercial cultivation process for <i>Agaricus bisporus</i>. Mycologia 109:475-484. https://doi.org/10.1080/00275514.2017.1349498

Pinzari F, Maggi O, Ceci A, Reverberi M, Persiani AM. 2017. Overlap in substrate utilisation and spatial exclusion in some microfungi which act as early cellulose colonisers in a Mediterranean environment. Pedobiologia 61:9-21. https://doi.org/10.1016/j.pedobi.2017.01.004

Řezáčová V, Konvalinková T, Jansa J. 2017. Carbon fluxes in mycorrhizal plants. In: Varma A, Prasad R, Tuteja N (eds.) Mycorrhiza: Eco-Physiology Secondary Metabolites Nanomaterials, Fourth Edition. Springer International, Basel (Switzerland) pp. 1-21. https://doi.org/10.1007/978-3-319-57849-1_1

Sapsford SJ, Paap T, Hardy GESJ, Burgess TI. 2017. The ‘chicken or the egg’: Which comes first forest tree decline or loss of mycorrhizae? Plant Ecology 218:1093-1106. https://doi.org/10.1007/s11258-017-0754-6

Schnittler M, Shchepin ON, Dagamac NHA, Dahl MB, Novozhilov YK. 2017. Barcoding myxomycetes with molecular markers: Challenges and opportunities. Nova Hedwigia 104:323-341. https://doi.org/10.1127/nova_hedwigia/2017/0397

Siddique AB, Khokon AM, Unterseher M. 2017. What do we learn from cultures in the omics age? High-throughput sequencing and cultivation of leaf-inhabiting endophytes from beech (<i>Fagus sylvatica</i> L.) revealed complementary community composition but similar correlations with local habitat conditions. MycoKeys 20:1-16. https://doi.org/10.3897/mycokeys.20.11265

Siletti CE, Zeiner CA, Bhatnagar JM. 2017. Distributions of fungal melanin across species and soils. Soil Biology and Biochemistry 113:285-293. https://doi.org/10.1016/j.soilbio.2017.05.030

Song Z, Kennedy PG, Liew FJ, Schilling JS. 2017. Fungal endophytes as priority colonizers initiating wood decomposition. Functional Ecology 31:407-418. https://doi.org/10.1111/1365-2435.12735

Soteras F, Ibarra C, Geml J, Barrios-García MN, Domínguez LS, Nouhra ER. 2017. Mycophagy by invasive wild boar (<i>Sus scrofa</i>) facilitates dispersal of native and introduced mycorrhizal fungi in Patagonia Argentina. Fungal Ecology 26:51-58. https://doi.org/10.1016/j.funeco.2016.11.008

Steinrucken TV, Raghavendra AKH, Powell JR, Bissett A, van Klinken RD. 2017. Triggering dieback in an invasive plant: Endophyte diversity and pathogenicity. Australasian Plant Pathology 46:157-170. https://doi.org/10.1007/s13313-017-0472-5

Strickland MS, Callaham MA, Jr. Gardiner ES, Stanturf JA, Leff JW, Fierer N, Bradford MA. 2017. Response of soil microbial community composition and function to a bottomland forest restoration intensity gradient. Applied Soil Ecology 119:317-326. https://doi.org/10.1016/j.apsoil.2017.07.008

Sun J-Y, Song Y, Ma Z-P, Zhang H-J, Yang Z-D, Cai Z-H, Zhou J. 2017. Fungal community dynamics during a marine dinoflagellate (<i>Noctiluca scintillans</i>) bloom. Marine Environmental Research 131:183-194. https://doi.org/10.1016/j.marenvres.2017.10.002

Vannette RL, Bichier P, Philpott SM. 2017. The presence of aggressive ants is associated with fewer insect visits to and altered microbe communities in coffee flowers. Basic and Applied Ecology 20:62-74. https://doi.org/10.1016/j.baae.2017.02.002

Wang J, Long T, Zhong Y, Li J, Zhang T, Feng Y, Lu Q. 2017. Disentangling the influence of climate soil and belowground microbes on local species richness in a dryland ecosystem of Northwest China. Scientific Reports 7:e18029. https://doi.org/10.1038/s41598-017-17860-7

Wilhelm RC, Cardenas E, Maas KR, Leung H, McNeil L, Berch S, Chapman W, Hope G, Kranabetter JM, Dubé S, Busse M, Fleming R, Hazlett P, Webster KL, Morris D, Scott DA, Mohn WW. 2017. Biogeography and organic matter removal shape long-term effects of timber harvesting on forest soil microbial communities. ISME Journal 11:2552-2568. https://doi.org/10.1038/ismej.2017.109

Yang T, Adams JM, Shi Y, He J-S, Jing X, Chen L, Tedersoo L, Chu H. 2017. Soil fungal diversity in natural grasslands of the Tibetan Plateau:associations with plant diversity and productivity. New Phytologist 215:756-765. https://doi.org/10.1111/nph.14606

Yurkov A, Pozo M.I. 2017. Yeast community composition and structure. In: Buzzini P, Lachance M-A, Yurkov A (eds.) Yeasts in Natural Ecosystems: Ecology.  Springer International, Basel (Switzerland) pp. 73-100. https://doi.org/10.1007/978-3-319-61575-2_3

Zhang K, Adams JM, Shi Y, Yang T, Sun R, He D, Ni Y, Chu H. 2017. Environment and geographic distance differ in relative importance for determining fungal community of rhizosphere and bulk soil. Environmental Microbiology 19:3649-3659. https://doi.org/10.1111/1462-2920.13865

Zhang J, Elser JJ. 2017. Carbon:Nitrogen:Phosphorus stoichiometry in fungi: A meta-analysis. Frontiers in Microbiology 8:e1281. https://doi.org/10.3389/fmicb.2017.01281

Zhang Z, Zhou X, Tian L, Ma L, Luo S, Zhang J, Li X, Tian C. 2017. Fungal communities in ancient peatlands developed from different periods in the Sanjiang Plain China. PLoS ONE 12:e0187575. https://doi.org/10.1371/journal.pone.0187575

Zheng Y, Hu H-W, Guo L-D, Anderson IC, Powell JR. 2017. Dryland forest management alters fungal community composition and decouples assembly of root- and soil-associated fungal communities. Soil Biology and Biochemistry 109:14-22. https://doi.org/10.1016/j.soilbio.2017.01.024


<b>2016</b>

Antunes PM, Koyama A. 2016. Mycorrhizas as nutrient and energy pumps of soil food webs: Multitrophic interactions and feedbacks. In: Collins-Johnson N, Gehring C, Jansa J (eds.) Mycorrhizal Mediation of Soil: Fertility Structure and Carbon Storage. Elsevier, Boston pp. 149-173. https://doi.org/10.1016/B978-0-12-804312-7.00009-7

Bálint M, Bahram M, Eren AM, Faust K, Fuhrman JA, Lindahl B, O'Hara RB, Öpik M, Sogin ML, Unterseher M, Tedersoo L. 2016. Millions of reads thousands of taxa: Microbial community structure and associations analyzed via marker genes. FEMS Microbiology Reviews 40:686-700. https://doi.org/10.1093/femsre/fuw017

Barnes CJ, Maldonado C, Frøslev TG, Antonelli A, Rønsted N. 2016. Unexpectedly high beta-diversity of root-associated fungal communities in the Bolivian Andes. Frontiers in Microbiology 7:e1377. https://doi.org/10.3389/fmicb.2016.01377

Benitez M-S, Taheri WI, Lehman R. 2016. Selection of fungi by candidate cover crops. Applied Soil Ecology 103:72-82. https://doi.org/10.1016/j.apsoil.2016.03.016

Burgess TI, Crous CJ, Slippers B, Hantula J, Wingfield MJ. 2016. Tree invasions and biosecurity: Eco-evolutionary dynamics of hitchhiking fungi. AoB PLANTS 8:plw076. https://doi.org/10.1093/aobpla/plw076

Chagnon P-L, Rineau F, Kaiser C. 2016. Mycorrhizas across scales: A journey between genomics global patterns of biodiversity and biogeochemistry. New Phytologist 209:913-916. https://doi.org/10.1111/nph.13819

Davey ML, Skogen MJ, Heegaard E, Halvorsen R, Kauserud H, Ohlson M. 2016. Host and tissue variations overshadow the response of boreal moss-associated fungal communities to increased nitrogen load. Molecular Ecology 26:571-588. https://doi.org/10.1111/mec.13938

Detheridge AP, Brand G, Fychan R, Crotty FV, Sanderson R, Griffith GW, Marley CL. 2016. The legacy effect of cover crops on soil fungal populations in a cereal rotation. Agriculture Ecosystems and Environment 228:49-61. https://doi.org/10.1016/j.agee.2016.04.022

Fernandez CW, Kennedy PG. 2016. Revisiting the 'Gadgil effect': Do inter-guild fungal interactions control carbon cycling in forest soils? New Phytologist 209:1382-1394. https://doi.org/10.1111/nph.13648

Giauque H, Hawkes CV. 2016. Historical and current climate drive spatial and temporal patterns in fungal endophyte diversity. Fungal Ecology 20:108-114. https://doi.org/10.1016/j.funeco.2015.12.005

Gornish ES, Fierer N, Barberán A. 2016. Associations between an invasive plant (<i>Taeniatherum caput-medusae</i> medusahead) and soil microbial communities. PLoS ONE 11:e0163930. https://doi.org/10.1371/journal.pone.0163930

Kivlin SN, Hawkes CV. 2016. Tree species spatial heterogeneity and seasonality drive soil fungal abundance richness and composition in Neotropical rainforests. Environmental Microbiology 18:4662-4673. https://doi.org/10.1111/1462-2920.13342

Lankau RA, Keymer DP. 2016. Ectomycorrhizal fungal richness declines towards the host species’ range edge. Molecular Ecology 25 (13):3224-3241. https://doi.org/10.1111/mec.13628

Liang M, Liu X, Gilbert GS, Zheng Y, Luo S, Huang F, Yu S. 2016. Adult trees cause density-dependent mortality in conspecific seedlings by regulating the frequency of pathogenic soil fungi. Ecology Letters 19:1448-1456. https://doi.org/10.1111/ele.12694

Rigg JL, Offord CA, Singh BK, Anderson IC, Clarke S, Powell JR. 2016. Variation in soil microbial communities associated with critically endangered Wollemi pine affects fungal but not bacterial assembly within seedling roots. Pedobiologia 59:61-71. https://doi.org/10.1016/j.pedobi.2016.02.002

Tedersoo L, Nilsson R.H. 2016. Molecular identification of fungi. In: Martin F (ed.) Molecular Mycorrhizal Symbiosis. John Wiley & Sons, New Jersey pp. 299-322. https://doi.org/10.1002/9781118951446.ch17

Toju H, Kishida O, Katayama N, Takagi K. 2016. Networks depicting the fine-scale co-occurrences of fungi in soil horizons. PLoS ONE 11:e0165987. https://doi.org/10.1371/journal.pone.0165987

Yang T, Sun H, Shen C, Chu H. 2017. Fungal assemblages in different habitats in an Erman's birch forest. Frontiers in Microbiology 7:e1368. https://doi.org/10.3389/fmicb.2016.01368


<b>Powered by: </b>

![alt text](http://www.stbates.org/images/mlab_logo.png)
