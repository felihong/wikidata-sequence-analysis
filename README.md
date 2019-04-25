# Wikidata Sequence Analysis
## Installing  
#### Create a virtual environment
We strongly suggest you using the virtual environment to install ores, to install Python’s virtual environment:
```
sudo apt install virtualenv
```
Create a directory named python-environments, then navigate in the newly created directory:
```
mkdir python-environments
cd python-environments
```
Create a virtual environment in Python 3 with the environment name of project_ores, then activate the newly created virtual environment:
```
virtualenv -p python3 project_ores
source ~/project_ores/bin/activate
```
Alternatively, you may also create the virtual environment by using package manager Anaconda:
```
conda create --name project_ores python=3.5.0
conda activate project_ores
```
#### Install ORES
To install ORES package in the virtual environment:
```
pip install ores
```
Or install directly the requirements:
```
pip install -r requirements.txt
```

## Revision Scoring 
The data can be fetched from the commandline using ORES built-in tools.
To pull a sample, start with:

```
head -n 5000 revision_id.csv | tsv2json int | ores score_revisions https://ores.wikimedia.org \
'Example app, here should be your user agend' \
wikidatawiki \
itemquality \
--input-format=plain \
--parallel-requests=4 \
> result.jsonlines
```
Please make sure that the input file revision_id.csv is beginning with a header "rev_id".

Then, the script itemquality_scores_to_csv.py could be used to parse results into CSV:
```
python itemquality_scores_to_csv.py < result.jsonlines > result.csv
```

## Data Sample

The sample data are collected mainly for the following two perspectives: 

* Descriptive statistics on sequences with the help of sequence pattern mining
* Sequence prediction by using Markov Chain 

#### Data Collection 
* Identify randomly 100 items per current quality prediction A, B, C, D, E, which are retrived from ```wikidatawiki_p page table : page_latest``` and ```ores API```
* The edit histories of all items are retrieved from ```wikidatawiki_p revision table```
* All data above would be combined again with the repective editer information from ```wikidatawiki_p user table```, together with edit comments from ```wikidatawiki_p comment table```, user group information from ```wikidatawiki_p user_groups table```


#### Data Scheme

| item_id | item_name | user_id | user_name | user_editcount | user_registration | user_group | comment | comment_simplified | operation | category | rev_id | rev_len | rev_timestamp | itemquality_prediction | itemquality_A | itemquality_B | itemquality_C | itemquality_D | itemquality_E | 
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---:|

* ```item_id``` edited page(item) ID
* ```item_name``` respective page(item) name 
* ```user_id```  editor ID
* ```user_name``` editer name 
* ```user_editcount``` rough number of edits and edit-like actions the user has performed
* ```user_registration``` editor registration timestamp
* ```user_group``` editor's user group and their corresponding user rights
* ```comment```  original comment information for this edit
* ```comment_simplified```  simplified comment information for this edit
* ```operation```  activity of the respective edit, retrieved from the simplified comment
* ```category```  term of the respective edit, explaining what kind of contents are exactly edited
* ```rev_id```  revision(edit) ID
* ```rev_len``` revision length
* ```rev_timestamp``` revision timestamp
* ```itemquality_prediction``` quality prediction of this revision ID, chosen as the one with the biggest probability 
* ```itemquality_A, itemquality_B, itemquality_C, itemquality_D, itemquality_E``` concrete quality level probability distribution of this revision