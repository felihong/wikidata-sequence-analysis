# Wikidata Sequence Analysis

## Installing  

## Data Sample

The sample data are collected mainly for the following two perspectives: 

* Descriptive statistics of data collected
* Bahaviour patterns with the help of sequence pattern mining

### Data Collection 
* Identify randomly 100 items per current quality prediction A, B, C, D, E, which are retrived from ```wikidatawiki_p page table : page_latest``` and ```ores API```
* The edit histories of all items are retrieved from ```wikidatawiki_p revision table```
* All data above would be combined again with the repective editer information from ```wikidatawiki_p user table```, together with edit comments from ```wikidatawiki_p comment table```, user group information from ```wikidatawiki_p user_groups table```

### Data Schema
| article_id | item_id | item_title | label | category|
| :---: | :---: | :---: | :---: | :---: |

* ```article_id``` table ID, primary key
* ```item_id``` edited item page ID
* ```item_title``` respective item page name 
* ```label``` English label of the item page
* ```category``` classified content category based on label and description

| editor_id | user_id | user_name | user_group | user_editcount | user_registration |
| :---: | :---: | :---: | :---: | :---: | :---: |

* ```editor_id```  table ID, primary key
* ```user_id```  editor ID
* ```user_name``` editer name 
* ```user_group``` editor's user group and their corresponding user rights
* ```user_editcount``` rough number of edits and edit-like actions the user has performed
* ```user_registration``` editor registration timestamp

| rev_id | prediction | itemquality_A | itemquality_B | itemquality_C | itemquality_D | itemquality_E |js_distance |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |  :---: |

* ```rev_id```  revision(edit) ID, primary key
* ```prediction``` quality prediction of this revision ID, chosen as the one with the biggest probability 
* ```itemquality_A, itemquality_B, itemquality_C, itemquality_D, itemquality_E``` concrete quality level probability distribution of this revision
* ```js_distance``` Jensen-Shannon divergence value based on given quality distribution

| rev_id | comment| edit_summary | edit_type | paraphrase |
| :---: | :---: | :---: | :---: | :---: | 

* ```rev_id``` revision(edit) ID, primary key
* ```comment```  original comment information for this edit
* ```edit_summary```  comment information simplified with regular expression
* ```edit_type```  schematized and classified edit summary for ease of use
* ```paraphrase```  paraphrase of edit summary according to Wikibase API 

| rev_id | parent_id | editor_id | article_id | rev_timestamp |
| :---: | :---: | :---: | :---: | :---: | 

* ```rev_id```  revision(edit) ID, primary key
* ```parent_id```  preceding revision(edit) ID
* ```editor_id```  foreign key to table editor 
* ```article_id```  foreign key to table article
* ```rev_timestamp``` revision timestamp

## ORES

### Installing
It is strongly suggested using virtual environment to install ores by firstly install python’s virtual environment and create a directory named python-environments, then navigate in the newly created directory:
```
sudo apt install virtualenv
mkdir python-environments
cd python-environments
```
Create a virtual environment in python 3 with the environment name of project_ores, then activate the newly created virtual environment:
```
virtualenv -p python3 project_ores
source ~/project_ores/bin/activate
```
Alternatively, you may also create the virtual environment with Anaconda:
```
conda create --name project_ores python=3.5.0
conda activate project_ores
```
Now install ORES package in the virtual environment:
```
pip install ores
```

### Revision Scoring 
The following steps show how to use ORES item_quality model scoring the given revisions as input, the data can be fetched from the commandline using the ORES built-in tools.

To pull a sample, start with:
```
revision_id.csv | tsv2json int | ores score_revisions https://ores.wikimedia.org \
'Example app, here should be your user agend' \
wikidatawiki \
itemquality \
--input-format=plain \
--parallel-requests=4 \
> result.jsonlines
```
Please make sure that the input file revision_id.csv is beginning with a header "rev_id". 

After this, the script itemquality_scores_to_csv.py could be used to parse results into CSV:
```
python itemquality_scores_to_csv.py < result.jsonlines > result.csv
```