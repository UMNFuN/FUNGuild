<h1>FUNGuild: Fungi + fUNctional + Guild</h1>

<b><i>Over 13,000 fungal taxa now included in the database</i>!</b>

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

Attwood GT, Wakelin SA, Leahy SC, Rowe S, Clarke S, Chapman DF, Muirhead R, Jacobs JME. 2019. Applications of the soil, plant and rumen microbiomes in pastoral agriculture. Frontiers in Nutrition 6:e107. https://doi.org/10.3389/fnut.2019.00107

Bai Z, Wu X, Lin J-J, Xie H-T, Yuan H-S, Liang C. 2019. Litter-, soil- and C:N-stoichiometry-associated shifts in fungal communities along a subtropical forest succession. Catena 178:350-358. https://doi.org/10.1016/j.catena.2019.03.037

Benucci GMN, Bonito V, Bonito G. 2019. Fungal, bacterial, and archaeal diversity in soils beneath native and introduced plants in Fiji, South Pacific. Microbial Ecology 78:136-146. https://doi.org/10.1007/s00248-018-1266-1

Birnbaum C, Hopkins AJM, Fontaine JB, Enright NJ. 2019. Soil fungal responses to experimental warming and drying in a Mediterranean shrubland. Science of the Total Environment 683:524-536. https://doi.org/10.1016/j.scitotenv.2019.05.222

Booth JM, Fusi M, Marasco R, Michoud G, Fodelianakis S, Merlino G, Daffonchio D. 2019. The role of fungi in heterogeneous sediment microbial networks. Scientific Reportsvolume 9:e7537. https://doi.org/10.1038/s41598-019-43980-3

Brinkmann N, Schneider D, Sahner J, Ballauff J, Edy N, Barus H, Irawan B, Budi SW, Qaim M, Daniel R, Polle A. 2019. Intensive tropical land use massively shifts soil fungal communities. Scientific Reports 9:e3403. https://doi.org/10.1038/s41598-019-39829-4

Carson CM, Jumpponen A, Blair JM, Zeglin LH. 2019. Soil fungal community changes in response to long-term fire cessation and N fertilization in tallgrass prairie. Fungal Ecology 41:45-55. https://doi.org/10.1016/j.funeco.2019.03.002

Chen L, Xiang W, Wu H, Ouyang S, Lei P, Hu Y, Ge T, Ye J, Kuzyakov Y. 2019. Contrasting patterns and drivers of soil fungal communities in subtropical deciduous and evergreen broadleaved forests. Applied Microbiology and Biotechnology 103:5421-5433. https://doi.org/10.1007/s00253-019-09867-z

Day NJ, Dunfield KE, Johnstone JF, Mack MC, Turetsky MR, Walker XJ, White AL, Baltzer JL. 2019. Wildfire severity reduces richness and alters composition of soil fungal communities in boreal forests of western Canada. Global Change Biology 25:2310-2324. https://doi.org/10.1111/gcb.14641

Egidi E, Delgado-Baquerizo M, Plett JM, Wang J, Eldridge DJ, Bardgett RD, Maestre FT, Singh BK. 2019. A few Ascomycota taxa dominate soil fungal communities worldwide. Nature Communications 10:e2369. https://doi.org/10.1038/s41467-019-10373-z

Geisen S, Briones MJI, Gan H, Behan-Pelletier VM, Friman V-P, Arjen de Groot G, Hannula SE, Lindo Z, Philippot L, Tiunovi AV, Wall DH. 2019. A methodological framework to embrace soil biodiversity. Soil Biology and Biochemistry 136:e107536. https://doi.org/10.1016/j.soilbio.2019.107536

Gómez FJR, Navarro-Cerrillo RM, Pérez-de-Luque A, Oβwald W, Andrea Vannini A, Morales-Rodríguez C. 2019. Assessment of functional and structural changes of soil fungal and oomycete communities in holm oak declined dehesas through metabarcoding analysis. Scientific Reports 9:e5315. https://doi.org/10.1038/s41598-019-41804-y

Grishkan I. 2019. Soil translocation at “Evolution Canyon” I (Mount Carmel, Israel) reveals the importance of microclimatic variation for structuring soil microfungal communities. Pedobiologia 75:8-14. https://doi.org/10.1016/j.pedobi.2019.04.002

Hannula SE, Zhu F, Heinen R, Bezemer TM. 2019. Foliar-feeding insects acquire microbiomes from the soil rather than the host plant. Nature Communications 10:e1254. https://doi.org/10.1038/s41467-019-09284-w

Koyama A, Maherali H, Antunes PM. Plant geographic origin and phylogeny as potential drivers of community structure in root-inhabiting fungi. Journal of Ecology 107:1720-1736. https://doi.org/10.1111/1365-2745.13143

Li J, Delgado-Baquerizo M, Wang J-T, Hu H-W, Cai Z-J, Zhu Y-N, Singh BK. 2019. Fungal richness contributes to multifunctionality in boreal forest soil. Soil Biology and Biochemistry 136:e107526. https://doi.org/10.1016/j.soilbio.2019.107526

Li PD, Jeewon R, Aruna B, Li HY, Lin FC, Wang HK. 2019. Metabarcoding reveals differences in fungal communities between unflooded versus tidal flat soil in coastal saline ecosystem. Science of The Total Environment 690:911-922. https://doi.org/10.1016/j.scitotenv.2019.06.473

Liu Y, Chen X, Liu J, Liu T, Cheng J, Wei G, Lin Y. 2019. Temporal and spatial succession and dynamics of soil fungal communities in restored grassland on the Loess Plateau in China. Land Degradation and Development 30:1273-1287. https://doi.org/10.1002/ldr.3289

Liu H, Khan MY, Carvalhais LC, Delgado-Baquerizo M, Yan L, Crawford M, Dennis PG, Singh B, Schenk PM. 2019. Soil amendments with ethylene precursor alleviate negative impacts of salinity on soil microbial properties and productivity. Scientific Reports 9:e6892. https://doi.org/10.1038/s41598-019-43305-4

Luo L, Zhang Z, Wang P, Han Y, Jin D, Su P, Tan X, Zhang D, Muhammad-Rizwan H, Lu X, Liu Y. 2019. Variations in phyllosphere microbial community along with the development of angular leaf-spot of cucumber. AMB Express 9:e76. https://doi.org/10.1186/s13568-019-0800-y

Makiola A, Dickie IA, Holdaway RJ, Wood JR, Orwin KH, Lee CK, Glare TR. 2019. Biases in the metabarcoding of plant pathogens using rust fungi as a model system. MicrobiologyOpen 8:e00780. https://doi.org/10.1002/mbo3.780

Maltz MR, Chen Z, Cao J, Arogyaswamy K, Shulman H, Aronson EL. 2019. Inoculation with <i>Pisolithus tinctorius</i> may ameliorate acid rain impacts on soil microbial communities associated with <i>Pinus massoniana</i> seedlings. Fungal Ecology 40:50-61. https://doi.org/10.1016/j.funeco.2018.11.011

Nagati M, Roy M, Desrochers A, Manzi S, Bergeron Y, Gardes M. 2019. Facilitation of balsam fir by trembling aspen in the boreal forest: Do ectomycorrhizal communities matter? Frontiers in Plant Science 10:e932. https://doi.org/10.3389/fpls.2019.00932

Ogwu MC, Takahashi K, Dong K, Song H-K, Moroenyane I, Waldman B, Adams JM. 2019. Fungal Elevational Rapoport pattern from a High Mountain in Japan. Scientific Reports 9:e6570. https://doi.org/10.1038/s41598-019-43025-9

Parladé J, Queralt M, Pera J, Bonet, JA, Castaño C, Martínez-Peña F, Piñol J, Senar MA, De Miguel AM. 2019. Temporal dynamics of soil fungal communities after partial and total clear-cutting in a managed <i>Pinus sylvestris</i> stand. Forest Ecology and Management 449:e117456. https://doi.org/10.1016/j.foreco.2019.117456

Pérez-Izquierdo L, Zabal-Aguirre M, González-Martínez SC, Buée M, Verdú M, Rincón A, Goberna M. 2019. Plant intraspecific variation modulates nutrient cycling through its below ground rhizospheric microbiome. Journal of Ecology, 107:1594-1605. https://doi.org/10.1111/1365-2745.13202

Phillips ML, Weber SE, Andrews LV, Aronson EL, Allen MF, Allen EB. 2019. Fungal community assembly in soils and roots under plant invasion and nitrogen deposition. Fungal Ecology 40:107-117. https://doi.org/10.1016/j.funeco.2019.01.002

Reazin C, Baird R, Clark S, Jumpponen A. 2019. Chestnuts bred for blight resistance depart nursery with distinct fungal rhizobiomes. Mycorrhiza 29:313-324. https://doi.org/10.1007/s00572-019-00897-z

Saitoh Y, Hirano S-I, Nagaoka T, Amano Y. 2019. Genetic survey of indigenous microbial eukaryotic communities, mainly fungi, in sedimentary rock matrices of deep terrestrial subsurface. Ecological Genetics and Genomics 12:e100042. https://doi.org/10.1016/j.egg.2019.100042

Saravesi K, Markkola A, Taulavuori E, Syvänperä I, Suominen O, Suokas M, Saikkonen K, Taulavuori K. 2019. Impacts of experimental warming and northern light climate on growth and root fungal communities of Scots pine populations. Fungal Ecology 40:43-49. https://doi.org/10.1016/j.funeco.2018.12.010

Schleuss P-M, Widdig M, Heintz-Buschart A, Guhr A, Martin S, Kirkman K, Spohn M. 2019. Stoichiometric controls of soil carbon and nitrogen cycling after long-term nitrogen and phosphorus addition in a mesic grassland in South Africa. Soil Biology and Biochemistry 135:294-303. https://doi.org/10.1016/j.soilbio.2019.05.018

Schroeder JW, Martin JT, Angulo DF, Arias-Del Razo I, Barbosa JM, Perea R, Sebastián-González E, Dirzo R. 2019. Host plant phylogeny and abundance predict root-associated fungal community composition and diversity of mutualists and pathogens. Journal of Ecology 107:1557-1566. https://doi.org/10.1111/1365-2745.13166

Schütte UME, Henning JA, Ye Y, Bowling A, Ford J, Genet H, Waldrop MP, Turetsky MR, White JR, Bever JD. 2019. Effect of permafrost thaw on plant and soil fungal community in a boreal forest: Does fungal community change mediate plant productivity response? Journal of Ecology 107:1737-1752. https://doi.org/10.1111/1365-2745.13139

Seaton FM, Jones DL, Creer S, George PBL, Smart SM, Lebron I, Barrett G, Emmett BA, Robinson SM. 2019. Plant and soil communities are associated with the response of soil water repellency to environmental stress. Science of The Total Environment 687:929-938. https://doi.org/10.1016/j.scitotenv.2019.06.052

Shi L, Feng W, Jing X, Zang H, Mortimer P, Zou X. 2019. Contrasting responses of soil fungal communities and soil respiration to the above- and below-ground plant C inputs in a subtropical forest. European Journal of Soil Science 70:751-764. https://doi.org/10.1111/ejss.12777

Wang Z, Jiang Y, Deane DC, He F, Shu W, Liu Y. 2019. Effects of host phylogeny, habitat and spatial proximity on host specificity and diversity of pathogenic and mycorrhizal fungi in a subtropical forest. New Phytologist 223:462-474. https://doi.org/10.1111/nph.15786

Wang Q, Ma M, Jiang X, Zhou B, Guan D, Cao F, Chen S, Li J. 2019. Long-term N fertilization altered 13C-labeled fungal community composition but not diversity in wheat rhizosphere of Chinese black soil. Soil Biology and Biochemistry 135:117-126. https://doi.org/10.1016/j.soilbio.2019.04.009

Wang G, Schultz P, Tipton A, Zhang J, Zhang F, Bever JD. 2019. Soil microbiome mediates positive plant diversity-productivity relationships in late successional grassland species. Ecology Letters 22:1221-1232. https://doi.org/10.1111/ele.13273

Weber SE, Diez JM, Andrews LV, Goulden ML, Aronson EL, Allen MF. 2019. Responses of arbuscular mycorrhizal fungi to multiple coinciding global change drivers. Fungal Ecology 40:62-71. https://doi.org/10.1016/j.funeco.2018.11.008

Würth DG, Dahl MB, Trouillie M, Wilmking M, Unterseher M, Scholler M, Sørensen S, Mortensen M, Schnittler M. 2019. The needle mycobiome of <i>Picea glauca</i> – A dynamic system reflecting surrounding environment and tree phenological traits. Fungal Ecology 41:177-186. https://doi.org/10.1016/j.funeco.2019.05.006

Xu YH, Brandl H, Osterwalder S, Elzinga EJ, Huang JH. 2019. Vanadium-basidiomycete fungi interaction and its impact on vanadium biogeochemistry. Environment International 130:e104891. https://10.1016/j.envint.2019.06.001

Yang W, Zhang D, Cai X, Xia L, Luo Y, Cheng X, An S. 2019. Significant alterations in soil fungal communities along a chronosequence of <i>Spartina alterniflora</i> invasion in a Chinese Yellow Sea coastal wetland. Science of The Total Environment 693:e133548. https://doi.org/10.1016/j.scitotenv.2019.07.354

Zhang Z-F, Cai L. 2019. Substrate and spatial variables are major determinants of fungal community in karst caves in Southwest China. Journal of Biogeography 46:1504-1518. https://doi.org/10.1111/jbi.13594

Gluck-Thaler E, Slot JC. 2018. Specialized plant biochemistry drives gene clustering in fungi. The ISME Journal 12:1694-1705. https://doi.org/10.1038/s41396-018-0075-3

Haelewaters D, Dirks AC, Kappler LA, Mitchell JK, Quijada L, Vandegrift R, Buyck B, Pfister DH. 2018. A Preliminary Checklist of Fungi at the Boston Harbor Islands. Northeastern Naturalist 25:45-76. https://doi.org/10.1656/045.025.s904

Asemaninejad, A, Thorn RG, Lindo Z. 2017. Vertical distribution of fungi in hollows and hummocks of boreal peatlands. Fungal Ecology 27:59-68. https://doi.org/10.1016/j.funeco.2017.02.002

Eisenhauer N, Antunes PM, Bennett AE, Birkhofer K, Bissett A, Bowker MA, Caruso T, Chen B, Coleman DC, de Boer W, de Ruiter P, DeLuca TH, Frati F, Griffiths BS, Hart MM, Hattenschwiler S, Haimi J, Heethoff M, Kaneko N, Kelly LC, Leinaas HP, Lindo Z, Macdonald C, Rillig MC, Ruess L, Scheu S, Schmidt O, Seastedt TR, van Straalen NM, Tiunov AV, Zimmer M, Powell JR. 2017. Priorities for research in soil ecology. Pedobiologia 63:1-7. https://doi.org/10.1016/j.pedobi.2017.05.003

Guise S, Kostenko O, Cnossen MC, ten Hooven FC, Vres B, van der Putten WH. 2017. Seed and root endophytic fungi in a range expanding and a related plant species. Frontiers in Microbiology 8:e1645. https://doi.org/10.3389/fmicb.2017.01645

Hui N, Jumpponen A, Francini G, Kotze DJ, Liu X, Romantschuk M, Strommer R, Setala H. 2017. Soil microbial communities are shaped by vegetation type and park age in cities under cold climate: Park soil microbial communities. Environmental Microbiology 19:1281-1295. https://doi.org/10.1111/1462-2920.13660

Jacobsen RM, Kauserud H, Sverdrup-Thygeson A, Bjorbaekmo MM, Birkemoe T. 2017. Wood-inhabiting insects can function as targeted vectors for decomposer fungi. Fungal Ecology 29:76-84. https://doi.org/10.1016/j.funeco.2017.06.006

McGee CF, Byrne H, Irvine A, Wilson J. 2017. Diversity and dynamics of the DNA and cDNA-derived compost fungal communities throughout the commercial cultivation process for Agaricus bisporus. Mycologia 109:475-484. https://doi.org/10.1080/00275514.2017.1349498

Nuske SJ, Vernes K, May TW, Claridge AW, Congdon BC, Krockenberger A, Abell SE. 2017. Redundancy among mammalian fungal dispersers and the importance of declining specialists. Fungal Ecology 27:1-13. https://doi.org/10.1016/j.funeco.2017.02.005

Oriol G, Geml J, Pérez-Haase A, Ninot JM, Semenova-Nelsen TA, Peñuelas J. 2017. Abrupt changes in the composition and function of fungal communities along an environmental gradient in the High Arctic. Molecular Ecology 26:4798-4810. https://doi.org/10.1111/mec.14227

Pinzari F, Maggi O, Ceci A, Reverberi M, Persiani AM. 2017. Overlap in substrate utilisation and spatial exclusion in microfungi that act as early cellulose colonisers in a Mediterranean environment. Pedobiologia 61:9-21. https://doi.org/10.1016/j.pedobi.2017.01.004

Siddique AB, Khokon AM, Unterseher M. 2017. What do we learn from cultures in the omics age? High-throughput sequencing and cultivation of leaf- inhabiting endophytes from beech (<i>Fagus sylvatica</i> L.) revealed complementary community composition but similar correlations with local habitat conditions. MycoKeys 20:1-16. https://doi.org/10.3897/mycokeys.20.11265

Soteras F, Ibarra C, Geml J, Barrios-García MN, Domínguez LS, Nouhra ER. 2017. Mycophagy by invasive wild boar (<i>Sus scrofa</i>) facilitates dispersal of native and introduced mycorrhizal fungi in Patagonia, Argentina. Fungal Ecology 26:51-58. https://doi.org/10.1016/j.funeco.2016.11.008

Vannette RL, Bichier P, Philpott SM. 2017. The presence of aggressive ants is associated with fewer insect visits to and altered microbe communities in coffee flowers. Basic and Applied Ecology 20:62-74. https://doi.org/10.1016/j.baae.2017.02.002

Zheng Y, Hu H-W, Guo L-D, Anderson IC, Powell JR. 2017. Dryland forest management alters fungal community composition and decouples assembly of root- and soil-associated fungal communities. Soil Biology & Biochemistry 109:14-22. https://doi.org/10.1016/j.soilbio.2017.01.024

Barnes CJ, Maldonado C, Froslev TG, Antonelli A, Ronsted N. 2016. Unexpectedly high beta-diversity of root-associated fungal communities in the Bolivian Andes. Frontiers in Microbiology 7:e1377. https://doi.org/10.3389/fmicb.2016.01377

Fernandez CW, Nguyen NH, Stefanski A, Han Y, Hobbie SE, Montgomery RA, Reich PB, Kennedy PG. 2016. Ectomycorrhizal fungal response to warming is linked to poor host performance at the boreal-temperate ecotone. Global Change Biology 23:1598-1609. https://doi.org/10.1111/gcb.13510

Leff JW, Lynch RC, Kane NC, Fierer N. 2016. Plant domestication and the assembly of bacterial and fungal communities associated with strains of the common sunflower, <i>Helianthus annuus</i>. New Phytologist 214:412-423. https://doi.org/10.1111/nph.14323

Liang M, Liu X, Gilbert GS, Zheng Y, Luo S, Huang F, Yu S. 2016. Adult trees cause density-dependent mortality in conspecific seedlings by regulating the frequency of pathogenic soil fungi. Ecology Letters 19:1448-1456. https://doi.org/10.1111/ele.12694

Semenova TA, Morgado LN, Welker JM, Walker MD, Smets E, Geml J. 2016. Compositional and functional shifts in arctic fungal communities in response to experimentally increased snow depth. Soil Biology and Biochemistry 100:201-209. https://doi.org/10.1016/j.soilbio.2016.06.001

Song Z, Kennedy PG, Lieu FJ, Schilling JS. 2016. Fungal endophytes as priority colonizers initiating wood decomposition. Functional Ecology 31:407-418. https://doi.org/10.1111/1365-2435.12735

Toju H, Kishida O, Katayama N, Takagi K. 2016. Networks depicting the fine-scale co-occurrences of fungi in soil horizons. PLoS ONE 11:e0165987. https://doi.org/10.1371/journal.pone.0165987

Yang T, Sun H, Shen C, Chu H. 2016. Fungal assemblages in different habitats in an Erman’s Birch Forest. Frontiers in Microbiology 7:e1368. https://doi.org/10.3389/fmicb.2016.01368

<b>Powered by: </b>

![alt text](http://www.stbates.org/images/mlab_logo.png)
