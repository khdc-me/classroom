#
#    Fetch headlines from The New York Times web site and write them,
#        as a list, to a text file. User will provide the file name to
#        use.
#

import requests
from bs4 import BeautifulSoup


def get_html(url):    
    '''
        Fetches HTML served at specified url and returns it raw
        
        returns string
    '''
    return requests.get(url).text


def get_headlines(html):
    '''
        Extracts Headline texts and joins then in way that each is in a separate line.
        
        returns string
    '''    
    # parse
    soup = BeautifulSoup(html)
    
    return "\n".join([str(headline.a.string).replace("\n", " ").strip() for headline in soup.find_all(class_="story-heading") if headline.a])


def get_file_name():
    fn = input("Enter desired filename:\n")
    
    return fn + '.txt'
    

def main():
    # get webpage's html code
    raw_html = get_html("http://newyorktimes.com/")
    
    filename = get_file_name()
    
    with open(filename, 'w') as open_file:
        open_file.write(get_headlines(raw_html))
    

if __name__ == "__main__":
    main()
