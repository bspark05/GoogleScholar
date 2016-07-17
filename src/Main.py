'''
Created on Jul 16, 2016

@author: Administrator
'''
import gscholar.gscholar as gscholar
from zs.bibtex.parser import parse_string

def GgscholarParsing(reference):
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

if __name__ == '__main__':
    ### Reading references from csv file
    
    
    ### Parsing the references
    
    article1 = GgscholarParsing("Geographically weighted regression: the analysis of spatially varying relationships")
    article2 = GgscholarParsing("Modeling spatial dimensions of housing prices in Milwaukee, WI")
    print(article1)
    print(article2)
    
    ### Saving the results in a graph DB`