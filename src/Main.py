#-*- coding: utf-8 -*-
'''
Created on Jul 16, 2016

@author: Administrator
'''

import gscholar.gscholar as gscholar
from zs.bibtex.parser import parse_string
import FileIO.Excel as excel
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import GS_Neo4j as neo4j


def gscholarParsing(reference):
#    output of gscholar.py
#    input dt - List
    gscResult = gscholar.query(reference)
    
#    parsing a series of strings in the list using zs.bibtex library
#    dt - zs.bibtex.structures.Bibliography (double dictionary)
    try:
        bibliography = parse_string(gscResult[0])
        #    parsing one dictionary of bibliography
        for key, value in bibliography.items():
            article = value
     
        return article
    #    return dt: zs.bibtex.structures.Article
    except(IndexError):
#         print gscResult
        return {} # empty dictionary
    


def articleToDictionary(article):
    dic = {}
    for keyUni, valueUni in article.items():
        key = str(keyUni)
        if type(valueUni) == list:
            value = []
            for elementUni in valueUni:
                element = str(elementUni)
                value.append(element)
        else:
            value = str(valueUni)
        dic[key] = value
    
    return dic
#    return dt: dictionary of string

if __name__ == '__main__':
    ### initiate GS_Neo4j class and activate the database
    neo4jCla = neo4j.GS_Neo4j('neo4j', 'bspark05')
    
    ### Reading references from csv file
    refers = excel.excelRead("Book4.xlsx", "Sheet1")
    
    referList = []
    for refer in refers:
        referStr = str(refer[0])
        referList.append(referStr)
        
        
    ### Parsing the references
#     for refer in referList:
#         print refer
#         article = gscholarParsing(refer)
#         dic = articleToDictionary(article)

    
    articleFrom = gscholarParsing("Basu, S., and T. G. Thibodeau. 1998. Analysis of spatial autocorrelation in house prices. Journal of Real Estate Finance and Economics 17 (1): 61–85.")
    dicFrom = articleToDictionary(articleFrom)
    print dicFrom
    
    articleTo = gscholarParsing(referList[1])
    print articleTo
    dicTo = articleToDictionary(articleTo)
    print dicTo
    
    
    ### Saving the results in a graph DB
    
#     neo4jCla.addRef()
    
    
    