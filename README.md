# Overview

This repo contains  code used for analysis of TCRB sequencing data from patients with colorectal liver metastasis (CLM) treated with long or short doses of chemotherapy compared to non-treated patients [1]. The data are deposited on the immuneACCESS database at the following [link](https://clients.adaptivebiotech.com/pub/ad7a2d37-a0bc-4d88-813e-6dd7d762a65b) with DOI: 10.21417/EH2023GS. The goal of this project is to understand the role of chemotherapy in reshaping the adaptive immune response in cancer.

This repo was created by Dennis Gong and Thomas Usherwood as part of the Biological Networks class at MIT (20.440). Please direct questions to dgong3@mit.edu and thomasu@mit.edu.

# Data

The data was generated using the [immunoSEQ hsTCRB Kit](https://www.immunoseq.com/) with samples obtained by Høye et al., with an abstract published in Cancer Research, accessible [here](https://aacrjournals.org/cancerres/article/82/12_Supplement/1346/699749/Abstract-1346-T-cell-receptor-repertoire). The dataset contains 92 samples, with 35 patients receiving neoadjuvant chemotherapy (NACT) for short interval and 15 patients receiving long interval NACT. An additional 35 patients did not receive NACT. All repertoires are stored in Adaptive ImmunoSEQ format. 

NOTE: The data files are large, so they are not included in the repository. When first cloning the repository, generate the required data folder structure using:
```
$ mkdir data
$ cd data/
$ mkdir analysis
$ mkdir processed
$ mkdir raw
$ cd ../
```

From the data listed above, populate ./data/raw/ with the sequencing files for each patient, and populate ./data/analysis with the sample overview file (both downloaded from the ImmunoSeq link above).

# Folder Structure

```
20.440-TCR-Analysis/
|__ README.md		
|__ notebooks/						
|__ src/ 						
	|__ data/ 					
	|__ analysis/ 				
	|__ visualization/ 			
	|__ util/ 					
|__ data/						
	|__ raw/					
		|__ ChemoProjTCRs/	
	|__ processed/				
	|__ analysis/				
		|__ SampleOverview.tsv		
|__ fig/ 						
	|__ main_fig/				
	|__ tables/					
	|__ supp_fig/				
```
'src' contains all scripts for generating results, which include scripts for cleaning data (data/), scripts for analyzing this cleaned data (analysis/), scripts for visualizing results (visualization/), and commonly reused scripts and helper functions (util/). In the data/ folder in the parent directory, raw data are stored in raw/ which contains all ImmunoSEQ formatted repertoires. Processed datasets and any intermediates are stored in processed/, and preprocessed data that are directly used for plotting are stored in analysis/. Exploratory notebooks are stored in the notebook/ directory in the parent directory. In the fig/ directory, there are three subdirectories used to store main figures, tables, and supplemental figures. The figure I generated for pset 4 is in `./fig/main_fig/unique_vdjgenes.jpg`
![Alt text](fig/main_fig/unique_vdj_genes.jpg?raw=true "Title")

# Installation

The driver file for the analysis in this pipeline is titled "driver.sh". The entire pipeline can be ran from `main.py`:
```
$ python main.py
```
Note that in the main function of main.py, there is a setting to toggle whether saved data generated previously (stored in `./data/processed/`) should be used to create plots, or whether data should be generated and saved from scratch. Toggle this by changing the `load_precalculated` variable.

Python package dependencies can be found in "requirements.txt". To intialize a virtual enviroment with these dependencies:
```
$ python -m venv venv
$ source ./venv/bin/activate
(venv) $ pip install -r requirements.txt
```

# References

1. Høye, E. et al. Abstract 1346: T cell receptor repertoire sequencing reveals chemotherapy-driven clonal expansion in colorectal liver metastases. Cancer Research 82, 1346 (2022).

