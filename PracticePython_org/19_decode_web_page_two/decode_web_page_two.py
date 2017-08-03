#
#    Program lets you navigate through The New York Times web site
#        - returns a list of all of the headlines in following format:
#            [0] This is the 1st Headline
#            [1] This is the 2nd Headline
#            [2] This is the 3rd Headline
#                    ...
#            [n] This is the nth Headline
#
#    You can now enter the number of a corresponding title to read the article or you can filter
#        the list by entering a keyword (ie: 'kittens'), and only titles that contain the keyword
#        will be displayed as a list like before. You are limited to only 1 keyword.
#
#    You can return to all headlines or filtered list from new article
#
#    Only text is retrieved (images, links, etc) ignored.
#

import requests
from bs4 import BeautifulSoup

def get_new_headlines():
    '''
        retrieve all headlines from NYTimes.com
        
        returns list
    '''
    # fetch and parse NYTimes's html
    raw_html = requests.get("https://www.nytimes.com/").text
    soup = BeautifulSoup(raw_html)
    
    # extract headings and link  into a list and return
    h2_soup = soup.find_all(class_="story-heading")

    # clean up and place target urls and anchor text into a list
    return [[link.a.get("href").strip(), str(link.a.string).strip()] for link in h2_soup if link.a and link.a.string]


def get_user_action(user_view, list_sorted, headline_list):
    '''
        Prompt user what he/she would like to do
        
        User can:
            - sort headlines by alphabetical order from a to z
            - sort headlines by alphabetical order from z to a
            - filter headlines that contain a specific keyword
                - toggle between filtered and all headlines
            - fetch new headlines
            - read article that belongs to a specific headline
            - from article, can return to filtered or all headlines
            
        returns string
    '''
    # do not display if reading an article
    if user_view in ("main", "filtered"):
        # display all headlines
        for i in range(20):
            print("\n")
            
        for i, headline in enumerate(headline_list):
            print("[" + str(i) + "]: " + headline[1])
    
    # prompt user for input
    if list_sorted == "asc":
        # currently sorted ascending
        sort_string = "Sort (desc)ending"
    elif list_sorted == "desc":
        # currently sorted descending
        sort_string = "Sort (asc)ending"
    else:
        # has no sorting (as displayed on NYT front page
        sort_string = "Sort (asc)ending | Sort (desc)ending"
        
    if len(headline_list) == 0:
        # no headlines (most likely after filtering)
        user_action = input("No articles with your desired keyword/filter. Please type 'f=none' to view list of headlines | (q)uit\n")
        while user_action.lower() != "f=none":
            # user typed something OTHER THAN 'f=none'
            user_action = input("You chose a keyword that is not present in any headline. Type f=none and press 'Enter' to view the complete list of headlines | (q)uit\n")
        
        return user_action # can only ever be 'f=none'
    elif len(headline_list) == 1:
        # only 1 headline (most likely after filtering)
        read_article_string = "Press 0 to read article"
    else:
        # more than 1 headline
        read_article_string = " 0 - " + str(len(headline_list)-1) + " to read article"
        
    if user_view == "main":
        # user viewing all headlines
        user_action = input(sort_string + " | " + read_article_string + "  | type a keyword to filter headlines | (r)eload headlines | (q)uit\n")            
    elif user_view == "filtered":
        # user viewing filtered headlines
        user_action = input(sort_string + " | " + read_article_string + " | type a keyword to further filter headlines | f=none to remove filter(s) and view all headlines | (q)uit\n")    
    else:
        # user viewing article
        user_action = input("Type 'back' to return to list of all headlines | (q)uit\n")
        while user_action not in ("q", "back"):
            #invalid input detected
            user_action = input("To return to the list of all headlines, type back and press the 'Enter' key | (q)uit\n")
    
    return user_action.lower()


def get_sorted_headlines(headline_list, asc_or_desc):
    '''
        sort headlines alphabetically by title, ascending (A to Z) or descending (Z to A)
        
        returns list
    '''
    if asc_or_desc == "asc":
        # sort ascending by heading title
        return sorted(headline_list, key=lambda headline: headline[1])
    else:
        # sort descending by heading title
        return sorted(headline_list, key=lambda headline: headline[1], reverse=True)
    
    
def get_filtered_headlines(headline_list, filter_string):
    '''
        filter out headlines that do not contain the word 'filter' in them
        
        returns list
    '''
    return [headline for headline in headline_list if filter_string in headline[1].lower()]


def get_article(headline_list, list_index):
    '''
        retrieve article text from url at list_index
        
        returns text
    '''
    list_index = int(list_index)
    
    # get title and url from headline list
    title = headline_list[list_index][1]
    url = headline_list[list_index][0]
    
    # fetch and parse NYTimes's html
    raw_html = requests.get(url).text
    soup = BeautifulSoup(raw_html)
    
    # extract headings and link  into a list and return
    p_soup = soup.find_all(class_="story-body-text")

    print("\n\n\n\n\n\n\n\n\n\n")
    print(title)
    print("\n\n".join([str(p.string).strip() for p in p_soup if p.string]))
    

def main():
    quit_browser = False
    make_soup = True
    
    while not quit_browser:
        if make_soup:
            # reload soup content
            all_headlines = get_new_headlines()
            
            view = "main"
            sort = "none"
            curr_headlines = all_headlines
            make_soup = False
        else:
            # continue working w/ cold soup (previously loaded data)
            usr_input = get_user_action(view, sort, curr_headlines)
            if usr_input.isnumeric() and int(usr_input) >= 0 and int(usr_input) <= len(curr_headlines):
                # action is a number between that represents a headline
                #    read corresponding article
                get_article(curr_headlines, usr_input)
                view = "article"
            elif usr_input == "asc":
                sort = "asc"
                # sort list from A to Z
                curr_headlines = get_sorted_headlines(curr_headlines, sort)
            elif usr_input == "desc":
                sort = "desc"
                # sort list from Z to A
                curr_headlines = get_sorted_headlines(curr_headlines, sort)
            elif usr_input in ("f=none", "back"):
                # clear filters, get all previously loaded headlines
                curr_headlines = all_headlines
                view = "main"   # reset view
            elif usr_input == "r":
                # fetch new set of headlines
                make_soup = True
            elif usr_input == "q":
                quit_browser = True
            else:
                # filter headlines
                curr_headlines = get_filtered_headlines(curr_headlines, usr_input)
                view = "filtered" # set to filtered view
        

if __name__ == '__main__':
    main()
