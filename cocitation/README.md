##Co-citation


This directory mainly include co-citation based therapy finding.


Authors cite articles since each one help authors.  
Even authors themselves hardly tell why they will cite two articles simultaneously.  
The co-occurrence in reference list is kind of latent knowledge. 

##Dataset
[PubMed Central](https://www.ncbi.nlm.nih.gov/pmc/)

##Procedures
To a given disease name "D", the procedures:

1. Fetch full text papers contained "D".
    
        python tools/xml_parser.py [D] [index path of pmc files] > paths.txt


2. From titles of references, stat the count of therapies co-occurrence with disease "D".


3. Filter and sort the therapies.

4. Human checking.


####Usage:


