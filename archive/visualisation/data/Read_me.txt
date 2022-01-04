Symbol	Explanation
Record_ID	Observation Number (from #1 to #588) #not important for modelling
Plot_ID	Plot Identification Letter (A to C) # important: choose by visual inspection on  location 
Replicate	"Replicate Code (1, 2 and 3)" # important: randomly selected
Web_ID	Unique combination of Plot ID and Replicate # replicate of one plot (site); match combination or record and plot id; to group them together; 
MajorGroup	"Main groups, here: size-defined binned groups (Bacteria, Fungi, Protozoa, Microfauna, Mesofauna, Macrofauna) and Plant roots (Plantae)"
PhylogeneticGroup	"Large Taxonomic Entities, here: Plantae, Fungi, Bacteria, Amoebae, Flagellatae, Nematoda, Collembola, Acarina, Enchytraeidae, Lumbricidae"
OTU	Operational Taxonomic Unit # sometimes species, sometimes genus, families, or not clear
Guild	Assigned Feeding Preference
Trophic_ID 	"The 2-digits Identification code: First number identifies the trophic preference, second number the phylogenetic group (see Trophic_ID synopsis)"
Taxon_ID	"The 5-digits  Identification code: First number identifies the trophic preference, second number the phylogenetic group, third,  fourth and fifth the taxon (see Taxon_ID synopsis)"
TrophicLevel	"The trophic level (1, 2 and 3) used to build the biomass pyramids"
Log10(Abundance)	Log population density (n / m^2) (OTU)
Log10(Mass)	Log site-specific body-mass average (µg dry weight) (OTU)
Log10(Biomass)	Log (Mass x Abundance)
TotalSoil-C	Carbon content in mmol  /  kg soil dry weight (refers to replicate)
TotalSoil-N	Nitrogen content in mmol / kg soil dry weight (refers to replicate)
TotalSoil-P	Phosphorus content in mmol / kg soil dry weight (refers to replicate)
Soil-pH	Soil pH in potassium chloride solution (1M KCl) # is log
	
Trophic_ID Synopsis	
36	Bacterivore amoebae
34	Bacterivore enchytraeid
37	Bacterivore flagellate
31	Bacterivore nematode
24	Fungivore enchytraeid
23	Fungivore insect 
21	Fungivore nematode
72	Generalist mite
12	Macrophytophage and panphytophage mite
22	Microphytophage mite (feeding on fungi)
82	Omnivore mite
81	Omnivore nematode
41	"Passive lifestage, substrate-related nematode"
13	Plant-feeding insect (springtail)
11	Plant-feeding nematode
51	Predating nematode (consuming nematodes)
62	Predatory mite (attacking arthropods)
52	Predatory mite (attacking nematodes)
92	Predatory mite (parasitizing mites and nematodes)
48	Primary (heterotrophic) producer
49	Primary (heterotrophic) producer
45	Substrate-ingesting earthworm
44	Substrate-inhabiting enchytraeid
#0	Primary (autotrophic) producer
	
Taxon_ID Synopsis	
* [FIRST KEY: THE 1st NUMBER (1 up to 9) PROVIDE INFORMATION ON THE MAIN FEEDING STRATEGY]	
*1	Plant-feeder
*2	Fungivore
*3	Bacterivore
*4	Substrate ingestion
*5	Predator of nematodes
*6	Predator of arthropods
*7	"General predator (predator of nematodes and of arthropods, but no parasitizing life stage)"
*8	"Omnivore (generalist, predator, plant-feeder and/or fungivore, possibly parasite)"
*9	Parasite (hosts are mites or nematodes; no passive dispersal of deutonymphs by phoresy)
*#	Primary (autotrophic) producer
** [SECOND KEY: THE 2nd NUMBER IDENTIFIES THE PHYLOGENETIC GROUP]	
**1	Nematoda
**2	Acarina
**3	Collembola
**4	Enchytraeidae
**5	Lumbricidae
**6	Amoebae
**7	Flagellatae
**8	Bacteria
**9	Fungi
**9	Plantae
"[FINALLY, THE LAST THREE NUMBERS IDENTIFY THE TAXON (see Appendix B)] "	
	
Authentication Procedure:	
"For the Dryad data file entitled 'Mass–Abundance Relationships In A Grassland Field Experiment.txt', the sum of all the three columns Log(Abundance), Log(Mass) and Log(Biomass) must equal  4921.64"	
