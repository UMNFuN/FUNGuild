GENERAL NOTES

The FUNGuild bioinformatic tool is based on an original in-house python script referenced in Branco et al. 2013. PLoS One 8: 1–10. (http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0078295).

A current version of Python (https://www.python.org/) must be installed on the user’s local machine, before the FUNGuild script (https://github.com/UMNFuN/FUNGuild/blob/master/FUNGuild.py) can be used. The FUNGuild database is accessed by the python script remotely and, therefore, does not need to be loaded to the user’s local machine; however, the script must be able to access the internet to connect with the database.

An example OTU table has been provided in the FUNGuild GitHub repository (https://github.com/UMNFuN/FUNGuild/blob/master/OTU_table_example.csv) to demonstrate table formatting.

**************************************

CONTRIBUTING GUILD INFORMATION TO THE FUNGUILD DATABASE

Guild data for a particular fungal taxon should be entered into each of seven fields in the FUNGuild database (a tab delimited text flat file) hosted in a GitHub repository (https://github.com/UMNFuN/FUNGuild/FUNGuild_DB.txt). Data can be contributed to the FUNGuild database in two manners: 1) indirectly by contacting the db curator (Nhu Nguyen: xerantheum@gmail.com); 2) directly by editing the FUNGuild database file in the GitHub repository and creating a pull request (see instructions below).

Information should be entered into each FUNGuild database field, in sequence, as follows:

- Taxon: Enter the scientific name of the taxon.

- Taxon Level: Enter a numeral corresponding the correct taxonomic level of the taxon (1 = phylum, 2 = sub phylum, 3 = class, 4 = sub class, 5 = order, 6 = family, 7 = genus, 8 = species (0 = keyword).

- Trophic Mode: Enter one of four trophic categories as follows - pathotroph = receiving nutrients at the expense of the host cells and strictly causing disease; symbiotroph = receiving nutrients by exchanging resources with host cells; saprotroph = receiving nutrients by breaking down dead host cells (these categories are similar with the concepts presented in Tedersoo et al. 2014. Global diversity and geography of soil fungi. Science 346(6213). DOI: 10.1126/science.1256688 (http://www.sciencemag.org/content/346/6213/1256688).

- Guild: Provide a relevant guild descriptor (e.g., animal pathogen, arbuscular mycorrhiza, dark septate endophyte, ectomycorrhiza, foliar endophyte, ericoid mycorrhiza, lichenicolous, lichenized, mycoparasite, undefined saprotroph, plant pathogen, wood saprotroph, etc). Construct new guilds as necessary.

- Confidence Ranking: “Highly Probable” (= absolutely certain), “Probable” (= fairly certain), “Possible” (= suspected but not proven, conflicting reports given, multiple associated guilds, etc.).

- Growth Morphology: basic morphological categories such as “yeast”, “facultative yeast”, “thallus” should be used.

- Trait: Functional or morphological traits such as “white rot” or “contact exploration type” would be appropriate for this column.

- Notes: Any other relevant information related to the taxon (e.g., “Facultative human pathogen causing coccidioidomycosis” for Coccidioides immitis).

- Citation/Source: Publication, website, etc. from which the corresponding guild information was derived (guild information for taxa that is based on peer-reviewed publications is preferred).

**************************************

FUNGuild database entries sent to the db curator should be in a table format [e.g., as a tab delimited text (.txt), comma-separated values (.csv), or Excel spreadsheet (.xls) file] with appropriate column headings (i.e., Taxon, Taxon Level, Trophic Category, Guild, Confidence Ranking, Growth Morphology, Trait, Notes, Citation/Source).

Otherwise, entries can be submitted directly by editing the FUNGuild database flat file in the GitHub repository and then creating a pull request to be reviewed and committed by the db curator. Editing/pull requests can be made as follows:

- Sign into your GitHub user account (or create one if needed here https://github.com/join).

- Navigate to the FUNGuild database flat file in your browser (https://github.com/UMNFuN/FUNGuild/blob/master/FUNGuild_DB.txt)

- On the FUNGuild_DB.txt file GitHub webpage click on the editing icon (a small pencil just above the file content).

- Add FUNGuild database taxon entries by directly making changes to the FUNGuild_DB.txt flat file under the ‘Edit file’ tab. First, scroll to a new line (numbers corresponding to each line should be visible to the right of the file content) at the bottom of the page in the FUNGuild_DB.txt flat file (if a new line is not available, place your cursor at the end of the last entry at the bottom of the page, and then hit return on your computer keyboard to create one). Next, input your taxon entry on the new line by sequentially typing information for each field in the database according to the format indicated above. Information for each database field entry should be separated by a single tab and each taxon entry should be separated by a single return. For example, on the new line type “Coccidioides immitis<tab>8<tab>Pathotroph<tab>Animal pathogen<tab>Highly Probable<tab><tab><tab>Facultative parasites causing coccidioidomycosis<tab>Bowman BH, Taylor JW, White TJ. Molecular Biology and Evolution 9: 893-904” (note: <tab> represents hitting the 'tab' bar on your computer keyboard rather than a word to be typed). An alternative way to do this is by entering data into each cell in a spreadsheet, then copy the finished entries into the FUNGuild_DB.txt flat file. This way is probably better since there is less of a chance of making mistakes by omission of one of the columns.

- Create a pull request for the proposed changes to the database by clicking on the ‘Propose file change’ button toward the bottom of the GitHub webpage page (an extended description or additional notes can be added by typing into the proposed change text field before clicking the button or into the ‘Write’ text field after clicking the button).

- The pull request can then be made by clicking on the ‘Create pull request’ button (a repository fork will be created and the db curator will be notified, automatically, once the button has been clicked on).

- The taxon entries that you have proposed for database will be visible on the FUNGuild_DB.txt flat file in the GitHub repository (https://github.com/UMNFuN/FUNGuild/blob/master/FUNGuild_DB.txt) once they have been reviewed and committed to the file by the FUNGuild db curator. Once committed to the FUNGuild_DB.txt flat file, your taxon entries will automatically be available to all using FUNGuild (https://github.com/UMNFuN/FUNGuild/blob/master/FUNGuild.py) to make fungal guild assignments to their OTU tables.

