## Co-citation


This directory mainly include co-citation based therapy finding.


Authors cite articles since each one help authors.  
Even authors themselves hardly tell why they will cite two articles simultaneously.  
The co-occurrence in reference list is kind of latent knowledge. 

## Dataset
[PubMed Central](https://www.ncbi.nlm.nih.gov/pmc/)

## Procedures
To a given disease name "D", the procedures:

1. Fetch full text papers contained "D".
    
        python tools/xml_parser.py [D] [index path of pmc files] > paths.txt


2. From titles of references, stat the count of therapies co-occurrence with disease "D".

        python cocitation/co-citation-finding.py ref [paths.txt] > pmc_refereces_title.txt
        python tools/np_extractor.py [D]_NPs.txt pmc_refereces_title.txt 1>>[D]_NPs.txt 2>run.log 


3. Filter the therapies.
        
        python tools/therapy_filter.py [D]_NPs.txt > [D]_ref_df.txt

4. Get the co-occurrence count of each therapies in body text in pmc articles.
        
        python tools/co-citation-finding.py tf [pmc index path] [[D]_ref_df.txt] 1>tf.txt 2>run.log

5. Calculate score of each therapy
        
        python tools/co-citation-finding.py score [[D]_ref_df.txt] [tf.txt] > score.txt

6. Human checking



