"""
Author: Gavin Mallott
Created: October 3, 2017
Lasted Edited: October 10, 2017
"""


#################################
## TO DO:                      ##
##                             ##
## Manage in-line <code> tags  ##
## Manage <ul> and <li> tags   ##
## Set up hyperlinks           ##
## Edit main page              ##
## Make things bold            ##
##                             ##
#################################


import requests
import re
from bs4 import BeautifulSoup, Comment


class AssignmentData(object):
    """Returns '<p>' tags in a selected html document based on Professor David Kay's lab assignments"""

    def __init__(self, url):
        '''Create an AssignmentData object by passing the url for the html document you want to parse'''
        what_i_want = url
        html = requests.get(what_i_want)
        self.soup = BeautifulSoup(html.text, 'lxml')

        self.p_prep = self.preparation()
        self.p_lab = self.lab_work()
        self.p_turnin = self.turnin()
        self.p_start = self.start()
        self.p_end = self.end() 

    def get_headers(self):
        """Find the undefinded list entries such as (1), (a), or Preparation"""
        headers = self.soup.find_all('strong')

        numbers = []
        words = []
        letters = []

        for head in headers:
            new_head = re.sub('[(\ ):]', '', head.text)
            try:
                new_head = int(new_head)
                numbers.append(new_head)
            except ValueError:
                words.append(new_head)

        letters = [x for x in words if len(x) < 4]
        words = [x for x in words if len(x) > 4]

        return numbers, words, letters

    def preparation(self):
        '''Get all <p> tags in the Preparation section'''
        paragraphs = self.soup.find_all('p')

        counter = 0
        prep_start = 0
        lab_start = 0

        for p in paragraphs:
            if "Lab Work" in p.text:
                lab_start = counter
            if "Preparation" in p.text:
                prep_start = counter
            counter += 1

        p_prep = [p for p in paragraphs[prep_start:lab_start-1]]

        return p_prep

    def lab_work(self):
        '''Get all <p> and <pre> tags in the Lab Work section'''
        everything = self.soup.find_all(['p', 'pre'])

        counter = 0
        lab_start = 0
        turnin_start = 0

        for comments in self.soup.find_all(text=lambda text:isinstance(text, Comment)):
            comments.extract()

        for tag in everything:
            if "Lab Work" in tag.text:
                lab_start = counter
            if "What to turn in:" in tag.text:
                turnin_start = counter
            else:
                pass
            counter += 1
        
        p_lab = [tag for tag in everything[lab_start+1:turnin_start]]

        return p_lab

    def turnin(self):
        '''Get all <p> tags within the Turn In section'''
        paragraphs = self.soup.find_all('p')

        counter = 0
        turnin_start = 0

        for p in paragraphs:
            if "What to turn in" in p.text:
                turnin_start = counter
            counter += 1

        p_turnin = [p for p in paragraphs[turnin_start:len(paragraphs)-2]]

        return p_turnin

    def start(self):
        '''Get all <p> tags between the beginnning of the assignment and the preparation section'''
        paragraphs = self.soup.find_all('p')

        counter = 0
        prep_start = 0

        for p in paragraphs:
            if p.text == "Preparation (Do this part individually; you can extend it past Friday if necessary)":
                prep_start = counter
            if p.text == "Preparation (Do this part individually, before coming to lab)":
                prep_start = counter
            counter += 1

        p_start = [p for p in paragraphs[0:prep_start-1]]

        return p_start

    def end(self):
        '''Get all <p> tags between the Turn In section and the end of the assignment'''
        paragraphs = self.soup.find_all('p')

        counter = 0
        end = 0

        for p in paragraphs:
            if "Written by David" in p.text:
                end = counter
            counter += 1

        p_end = paragraphs[end]

        return p_end

    def get_links(self, tag_list):
        '''Separate <a> tags by passing in a list of enclosing <p> tags'''
        links = [link.a for link in tag_list if link.a != None]
        hrefs = []
        for link in links:
            hrefs.append(link.get('href'))

        print(links)
        print(hrefs)


if __name__ == '__main__':   
    lab0 = AssignmentData('http://www.ics.uci.edu/~kay/courses/31/hw/lab0.html')
    #print(''.join(lab0.start()))
    #print(len(lab0.lab_work()))
    lab1 = AssignmentData('http://www.ics.uci.edu/~kay/courses/31/hw/lab1.html')
    lab1.get_links(lab1.p_lab)

    #print(lab1.lab_work())