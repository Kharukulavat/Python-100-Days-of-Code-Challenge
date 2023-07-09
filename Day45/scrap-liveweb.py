from bs4 import BeautifulSoup
import requests
response = requests.get('https://news.ycombinator.com/news')
# print(response.text) #> whole HTML of the website

yc_web_page = response.text
soup = BeautifulSoup(yc_web_page, 'html.parser')

#Get the title, url, upvote of the first article using BeautifulSoup
article_tag = soup.find(name = 'a', rel = 'noreferrer')
# article_tag = soup.find(name = 'a', class_ = 'storylink') //Follows Angela Yu

article_text = article_tag.getText()
article_link = article_tag.get('href')
article_upvote = soup.find(name = 'span', class_ = 'score').getText()
# we add getText() b/c otherwise, it will just gets us the tag
print(article_text)
print(article_link)
print(article_upvote)


#Get the title of all articles using BeautifulSoup
articles = soup.find_all(name = 'a', rel = 'noreferrer')
# article_tag = soup.find_all(name = 'a', class_ = 'storylink') //Follows Angela Yu
article_texts = []
article_links = []
for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get('href')
    article_links.append(link)
    
article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name = 'span', class_ = 'score')] # .split()[0]get hold of the actual number from the upvotes (cut the 'points' out) -> ['72 points'] -> ['72', 'points'] -> ['72']

# print(article_texts)
# print(article_links)
# print(article_upvotes)
# print(article_upvotes[0].split()[0]) 

#print out the title and link with the highest number of votes

#My solution
highest_upvotes_article = []
for i, upvote in enumerate(article_upvotes):
    if upvote == max(article_upvotes):
        highest_upvotes_article.append(article_texts[i])
        highest_upvotes_article.append(article_links[i])
        highest_upvotes_article.append(upvote)
print(highest_upvotes_article)

#Angela Yu's solution
largest_number = max(article_upvotes)
print(largest_number)
