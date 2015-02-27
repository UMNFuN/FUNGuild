
<h2>FUNGuild: Fungi + fUNctional + Guild</h2>

**************************************

https://github.com/UMNFuN/FUNGuild

http://glimmer.rstudio.com/stbates/FUNGuild/

http://glimmer.rstudio.com/stbates/FUNGuildUpload/

**************************************

GENERAL NOTES

The FUNGuild bioinformatic tool is based on an original in-house python script referenced in Branco et al. 2013. PLoS One 8: 1–10 (http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0078295).

A current version of Python (https://www.python.org/) must be installed on the user’s local machine, before the FUNGuild script (https://raw.githubusercontent.com/UMNFuN/FUNGuild/master/FUNGuild_v1.0.py) can be used. The FUNGuild database is accessed by the python script remotely and, therefore, does not need to be loaded to the user’s local machine. However, the script must be able to access the internet to connect with the database.

An example OTU table has been provided in the FUNGuild GitHub repository (https://github.com/UMNFuN/FUNGuild/blob/master/otu_table_example.txt) to demonstrate table formatting.

CONTRIBUTING GUILD INFORMATION TO THE FUNGUILD DATABASE

Data pertaining to particular fungal taxa can be submitted to the FUNGuild database as single (inputted via an online user interface - http://glimmer.rstudio.com/stbates/FUNGuild/) or multiple (inputted online as a tab delimited text file - http://glimmer.rstudio.com/stbates/FUNGuildUpload/). All submitted entries will be reviewed by the database curators prior to being migrated to the main FUNGuild DB.

**************************************

Information should be entered into each FUNGuild database field, in sequence, as follows:

    •    Taxon: The scientific name (e.g., Ganoderma).

    •    Taxon Level: A numeral corresponding the correct taxonomic level of the taxon (1 = phylum, 2 = sub phylum, 3 = class, 4 = sub class, 5 = order, 6 = family, 7 = genus, 8 = species, 0 = keyword).

    •    Trophic Mode: One of three trophic categories (pathotroph = receiving nutrients at the expense of the host cells and causing disease; symbiotroph = receiving nutrients by exchanging resources with host cells; saprotroph = receiving nutrients by breaking down dead host cells). The concepts presented here are similar to those of Tedersoo et al. 2014. Global diversity and geography of soil fungi. Science 346(6213). DOI: 10.1126/science.1256688 (http://www.sciencemag.org/content/346/6213/1256688).

    •    Guild: Provide a relevant guild descriptor (e.g., Animal Pathogen, Arbuscular Mycorrhiza, Dark Septate Endophyte, Ectomycorrhiza, Foliar Endophyte, Ericoid Mycorrhiza, Lichenicolous, Lichenized, Mycoparasite, Undefined Saprotroph, Plant Pathogen, Wood Saprotroph, etc). New guilds can be erected if necessary.

    •    Confidence Ranking: “Highly Probable” (= absolutely certain), “Probable” (= fairly certain), “Possible” (= suspected but not proven, conflicting reports given, multiple associated guilds, etc.).

    •    Growth Morphology: basic morphological categories such as Gasteroid Fungus, Mushroom, Facultative Yeast, Yeast, or Thallus should be noted.

    •    Trait: Functional or morphological traits such as “White Rot” or “Contact Exploration Type” would be appropriate for field.

    •    Notes: Any other relevant information related to the taxon (e.g., “Facultative human pathogen causing coccidioidomycosis” for Coccidioides immitis).

    •    Citation/Source: Publication, website, etc. from which the corresponding guild information was derived (e.g., Tedersoo L, May TW, Smith ME. 2010. Mycorrhiza 20: 217-263). Data for taxa that is based on peer-reviewed publications is preferred.
    
**************************************

The taxon entries that you have proposed for addition to the database will be visible on the FUNGuild DB once they have been reviewed by the DB curators and migrated to the main database (taxon queries to the FUNGuild DB can be carried out via the single entry user interface at http://glimmer.rstudio.com/stbates/FUNGuild/). 

Once migrated, your entries will automatically be available to all using the FUNGuild bioinformatic tool to make annotated assignments (e.g., guilds) to their OTU tables of fungal taxa.

