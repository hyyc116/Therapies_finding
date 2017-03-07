#coding:utf-8
import sys
from bs4 import BeautifulSoup as bs


def parse_doc(path):
    doc = bs(open(path).read(),'lxml')
    return doc

def parse_with_selector(doc,selector):
    return doc.select(selector)


def parse_pmc_references(path):
    doc = parse_doc(path)
    eles =parse_with_selector(doc,'ref-list ref article-title')
    for ele in eles:
        yield ele.get_text().strip()

def filter_papers_with_disease(name,indexpath):
    for path in open(indexpath):
        path = path.strip()
        titles = []
        for title in parse_pmc_references(path):
            titles.append(title)

        if name in ".".join(titles).lower():
            print path

if __name__=="__main__":
    filter_papers_with_disease(sys.argv[1],sys.argv[2])


