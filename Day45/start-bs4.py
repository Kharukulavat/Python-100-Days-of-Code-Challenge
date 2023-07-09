import requests
from bs4 import BeautifulSoup
#import lxml
with open("website.html") as file:
    contents: str = file.read()
soup: BeautifulSoup = BeautifulSoup(contents, 'html.parser')
# soup = BeautifulSoup(contents, 'lxml')

# print(soup.title) #<title>Angela's Personal Site</title>
# print(soup.title.name) #title
# print(soup.title.string) #Angela's Personal Site
# print(soup) #print the whole html
# print(soup.prettify()) #indent the soup HTML code; easier to read
# print(soup.a) #gives the first anchor tag found in website
# print(soup.li) #first li
# print(soup.p) #first paragraph

all_anchor_tags = soup.find_all(name = 'a')
print(all_anchor_tags) #> [<a href="https://www.appbrewery.co/">The App Brewery</a>, <a href="https://angelabauer.github.io/cv/hobbies.html">My Hobbies</a>, <a href="https://angelabauer.github.io/cv/contact-me.html">Contact Me</a>]

for tag in all_anchor_tags:
    print(tag.getText()) #print out all the text in anchor tag ex. The App Brewery
    print(tag.get('href')) #give all the links ex. https://www.appbrewery.co/

heading = soup.find(name = 'h1', id = 'name') #This will give that pareticular element
print(heading) #> [<h1 id="name">Angela Yu</h1>]

section_heading = soup.find(name = 'h3', class_ = 'heading') #use class_ for attribute
print(section_heading) #> <h3 class="heading">Books and Teaching</h3>
print(section_heading.getText())#> Books and Teaching
print(section_heading.name) #> h3
print(section_heading.get('class')) #> ['heading']

#HTML Selector
#select_one gives the first matching, and select will give all of the matching items in a list
company_url = soup.select_one(selector = "p a") #we're looking for an 'a' tag inside 'p' tag
print(company_url) #> <a href="https://www.appbrewery.co/">The App Brewery</a>

#we can also use the class or the id in CSS Selector
#the 'selector' is the first item that goes into the method, so we can have 'selector' keyword or not having it
name = soup.select_one(selector = '#name') #To select 'id' we use '#' sign
#or name = soup.select_one('#name')
print(name) #> <h1 id="name">Angela Yu</h1>

headings = soup.select('.heading') #select all the elements that have a class of heading, this is going to be a list
print(headings) #> [<h3 class="heading">Books and Teaching</h3>, <h3 class="heading">Other Pages</h3>]