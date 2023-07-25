import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)

#The raw HTML text
website_html = response.text 
# print(web_page)

soup = BeautifulSoup(response.content, 'html.parser')
# print(soup.prettify())

all_movies = soup.find_all(name = "h3", class_ = "title")
sorted_all_movies = []
movie_titles = [movie.getText() for movie in all_movies]
# for title in all_movies:
#     sorted_all_movies.append(title.getText())

#Print the movie titles in reverse order (from last to first) using slicing:
print(movie_titles[::-1]) #This will reverse the order

#The reverse method 
# sorted_all_movies.reverse()
# for movie in sorted_all_movies:
#     print(movie)

#print the movie titles in reverse order using a for loop:
for n in range(len(movie_titles) - 1, -1, -1):
    print(movie_titles[n])

#Reverse the movie_titles list and write the movie titles to a file named "movies.txt":
movies = movie_titles[::-1]
with open ("movies.txt", mode="w") as file:
    for movie in movies:
        file.write(f"{movie}\n") #Wtite the name of the movie

#The script will create a file named "movies.txt" in the same directory as the Python script and write the movie titles in reverse order to it. Each movie title will be on a separate line.

