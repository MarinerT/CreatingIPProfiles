# Creating IP-based Profiles for Document Recommendation on EDGAR


### Project Description & Motivation

EDGAR log file set has a wealth of information about (masked) IP addresses and which documents the ip address attempted to access. This project aims to create a log of similar documents like a Page Rank based upon the IP paths over the course of a day. 

The applicability of the model could serve investigators looking into possible networks amongst anonymous IP addresses. It could also possibly detect latent social networks or grouped similar behavior. 

### Background

EDGAR is the Securities and Exchange Commission's database for accessing publicly available financial & ownership information about publicly traded companies. Millions of people across the world access the database, including crawlers from large institutions like Bloomberg and smaller investors.

### Github Structure
* data: contains the sample log data.
* worksheet: contains the Jupyter Notebooks.
* scripts: contains the scripts used in ETL.
* img: will contain the graph images to be used on the README.

### Exploratory Data Analysis

#### Assumptions

1. All events are independent. 
2. All documents were obtained.
3. Crawlers used are represented in the higher range of document acquisition.


#### The Source: EDGAR Log File Dataset
Source: https://www.sec.gov/dera/data/edgar-log-file-data-set.html

Log for 10 OCT 2010

To obtain the data, go to the above site and download the log file log20101010.zip.

#### Features of the Dataset

Total Attributes: 16
Key Features: ip, date, time, accession
Feature Engineered: datetime, ip_ccount, doc_ccount, ip_total_count, doc_total_count, toDoc

#### Basic Log & Sample Numbers

Events: 2,136,342
Sample Size: 16,413

Documents in Original: 959,850
Documents in Sample: 4,361

IPs in Original: 14,277
IPs in Sample: 231

#### Network Features

Type: Graph
Number of nodes: 4333
Number of edges: 7929
Average degree:   3.6598

### Pipeline

*Extract*
* Uploaded log files to S3 bucket.
* Read log file into a Pandas DataFrame.

*Transform*
* Reformatted date columns & dropped unused attributes
* Featured engineered columns for filtering events by number of number of total hits by ip and number of total hits per document (accession). 
* Feature engineered the toDoc column in order to obtain a path of from the document to the next document.

*Load*
* Loaded the document into NetworkX graphing to visualize the network and obtain degrees of centrality and betweenness.

### Modelling & Validation

The data is unlabeled and requires unsupervised learning techniques. Looking at the Network graph, there appears to be very popular documents, but there does not appear to be separate clusters or clear separate paths. Looking at Kernel Density with tophat and gaussian kernel, albeit using the wrong type of numbers, reflect the same concept that there aren't any peaks or groups of documents.  


### Conclusion & Further Steps

Due to bad assumptions, bad data wrangling and modelling, nothing can be inferred from the dataset about detecting document rank and paths of ips.  Within the data one ip address would represent a large company, and within seconds would hit the same document. This does illustrate that group behavior does exist within the dataset, but the model needs a better algorithm that could detect and label the separate users. 
