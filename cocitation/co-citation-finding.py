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
    find_doc_count=0
    tf_dic=defaultdict(list)
    for path in open(indexpath):
        count+=1
        if not path.strip().endswith('.nxml'):
            continue

        if count%10==1:
            sys.stderr.write('PROGRESS:{:},'.format(count))
            sys.stderr.write('find {:} docs.\n'.format(find_doc_count))

        path = path.strip()

        
        content = open(path).read().lower()

        if "parkinson's disease"  not in content:
            continue

        find_doc_count+=1
        content = parse_body_abstext(path)
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


def score_therapies(df_path,tf_path):
    df_dict=defaultdict(int)
    tf_dict = defaultdict(int)
    for line in open(df_path):
        splits = line.split("\t")
        therapy = re.sub(r'\s+'," ",splits[0].replace("-"," "))
        df_dict[therapy]=int(splits[2])

    for line in open(tf_path):
        splits = line.split("\t")
        tf_dict[splits[0]] = int(splits[1])

    results=defaultdict(float)
    for t in df_dict.keys():
        tf = tf_dict.get(t,0.5)
        result[t]=df_dict[t]/float(tf)

    for k,v in sorted(results.items(),key=lambda x:x[1],reverse=True):
        print "{:}\t{:.5f}".format(k,v)



if __name__=="__main__":
    clas = sys.argv[1]
    if clas=='ref':
        parse_references_with_index(sys.argv[1])
    elif clas=='tf':
        indexpath=sys.argv[2]
        dfpath=sys.argv[3]
        nplist = [re.sub(r'\s+'," ",line.strip().split('\t')[0].replace("-"," ")) for line in open(dfpath)]
        parse_indexes(indexpath,nplist)
    elif clas=='score':
        score_therapies(sys.argv[1],sys.argv[2])






