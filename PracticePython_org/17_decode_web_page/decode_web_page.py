#
#    NYT headline retriever
#
#    List all of the headlines on https://www.nytimes.com/
#

import requests
from bs4 import BeautifulSoup


def getHTML(url):    
    '''
        Fetches HTML served at specified url and returns it raw
        
        returns string
    '''
    return requests.get(url).text


def getHeadLines(html):
    '''
        Extracts Headline texts and joins then in way that each is in a separate line.
        
        returns string
    '''    
    # parse
    soup = BeautifulSoup(html)
    
    return "\n".join([headline.a.string.replace("\n", " ").strip() for headline in soup.find_all(class_="story-heading") if headline.a and headline.a.string])
    

def main():
    # main body
    # get webpage's html code
    raw_html = getHTML("http://newyorktimes.com/")
    
    # get headlines
    print(getHeadLines(raw_html))


if __name__ == '__main__':
    main()
