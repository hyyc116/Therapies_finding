#coding:utf-8
import sys
sys.path.append(".")
sys.path.append("..")
from tools.xml_parser import *


#Get references
def parse_references_with_index(indexpath):
    for path in open(indexpath):
        path = path.strip()
        doc = parse_doc(path)
        titles = []
        for title in parse_pmc_references(doc):
            titles.append(title)

        headers = '. '.join(titles)+"."

        doi = parse_pmc_doi(doc)

        print doi+"\t"+unicode(headers,errors='ignore')

if __name__=="__main__":
    parse_references_with_index(sys.argv[1])




