#coding:utf-8
import sys
sys.path.append(".")
sys.path.append("..")
from tools.xml_parser import *
reload(sys)
sys.setdefaultencoding('utf-8')


#Get references
def parse_references_with_index(indexpath):
    count =0
    for path in open(indexpath):
        count+=1
        if not path.strip().endswith('.nxml'):
            continue

        if count%100==1:
            sys.stderr.write('{:}\n'.format(count))
        path = path.strip()
        doc = parse_doc(path)
        titles = []
        for title in parse_pmc_references(doc):
            titles.append(title)

        headers = '. '.join(titles)+"."

        doi = parse_pmc_doi(doc)

        print doi+"\t"+unicode(headers.encode('utf-8'),errors='ignore'）



if __name__=="__main__":
    parse_references_with_index(sys.argv[1])




