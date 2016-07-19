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


def gscholarParsing(reference):
#    output of gscholar.py
#    dt - List
    gscResult = gscholar.query(reference)
#    parsing a series of strings in the list using zs.bibtex library
#    dt - zs.bibtex.structures.Bibliography (double dictionary)
    bibliography = parse_string(gscResult[0])
#    parsing one dictionary of bibliography
    for key, value in bibliography.items():
        article = value
 
    return article
#    return dt: zs.bibtex.structures.Article

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
    
    ### Reading references from csv file
    refers = excel.excelRead("Book1.xlsx", "Book1")
    
    referList = []
    for refer in refers:
        referStr = str(refer[0])
        referList.append(referStr)
    
    
    ### Parsing the references
    article2 = gscholarParsing("Modeling spatial dimensions of housing prices in Milwaukee, WI")
    dic2 = articleToDictionary(article2)
    
    ### Saving the results in a graph DB