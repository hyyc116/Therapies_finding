#coding:utf-8
import sys
sys.path.append(".")
sys.path.append("..")
from tools.xml_parser import *
reload(sys)
sys.setdefaultencoding('utf-8')
import re
from collections import defaultdict
import json

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

        headers = re.sub(r"\s+",' ','. '.join(titles)+".")

        doi = parse_pmc_doi(doc)

        print doi+"\t"+headers.encode('utf-8')

#get body text
def parse_indexes(indexpath,nplist):
    count=0
    tf_dic=defaultdict(list)
    for path in open(indexpath):
        count+=1
        if not path.strip().endswith('.nxml'):
            continue

        if count%10==1:
            sys.stderr.write('{:}\n'.format(count))

        path = path.strip()
        content = parse_body_abstext(path)

        if "parkinson's disease"  not in content:
            continue

        content = re.sub(r'\s+'," ",content.replace('-'," ").lower())
        for np in nplist:
            if np in content:
                tf_dic[np].append(path)

    open("parkinson-tf.dict",'w').write(json.dumps(tf_dic))

    for np in tf_dic.keys():
        print np+"\t"+str(len(set(tf_dic[np])))
        

def parse_body_abstext(path):
    doc = parse_doc(path)
    content = doc.select('sec p')
    # abstext = doc.select('abstract')[0].get_text()
    ps=[]
    for p in content:
        ps.append(re.sub(r'\s+'," ",p.get_text()))

    return " ".join(ps)


if __name__=="__main__":
    clas = sys.argv[1]
    if clas=='ref':
        parse_references_with_index(sys.argv[1])
    elif clas=='parse_indexes':
        indexpath=sys.argv[2]
        dfpath=sys.argv[3]
        nplist = [re.sub(r'\s+'," ",line.strip().split('\t')[0].replace("-"," ")) for line in open(dfpath)]
        parse_indexes(indexpath,nplist)





