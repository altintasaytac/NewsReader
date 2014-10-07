import cookielib
from cookielib import CookieJar
import urllib2
import time
import re
import datetime


cj = CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
opener.addheaders = [('User-agent', 'Mozilla/5.0')]

conn = sqlite3.connect('kBase.db')
c = conn.cursor()
visitedLinks = ['http://topics.nytimes.com/top/news/international/countriesandterritories/turkey/index.html?rss=1']

def processor(data):
    tokenized = nltk.word_tokenize(data) 
    print tokenized
def NyTimesVisit():
    
    page = 'http://topics.nytimes.com/top/news/international/countriesandterritories/turkey/index.html?rss=1'

    sourceCode = opener.open(page).read()
  
    
    
    feedcontent = re.findall(r'<h2.*?>(.*?)</h2>',sourceCode)
    links = re.findall(r'<p.*?href="(.*?)"',str(sourceCode))
    
    for link in links:
        print link
        if link in visitedLinks:
            print "link already visited"
        else:
            visitedLinks.append(link)
            print 'visiting the link'
    
            print '########################'
            if link == 'http://topics.nytimes.com/top/news/international/countriesandterritories/turkey/index.html?rss=1':
                break
            else:
                linkSource = opener.open(link).read()

                linesOfInterest= re.findall(r'<p.*?>(.*?)</p>',linkSource)
                print 'Content:'
                for eachline in linesOfInterest:
                    if '<img width' in eachline:
                        pass
                    elif '<a href=' in eachline:
                        pass
                    elif '<div id=' in eachline:
                        pass
                    elif '<em' in eachline:
                        pass
                    elif '"\"' in eachline:
                        pass
                    else:
                        contsender = eachline.decode('utf-8')
                        processor(contsender)
                        
                
            time.sleep(5)
           
            
                
    
NyTimesVisit()   
