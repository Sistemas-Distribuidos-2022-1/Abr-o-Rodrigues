from bs4 import BeautifulSoup
import requests;

url = "https://trakt.tv/movies/trending";
f = requests.get(url);

sp = BeautifulSoup(f.content, "html.parser");
movies = sp.find_all(name="div", attrs={"data-type": "movie"});

print("Crawler busca os filmes listados na página principal do site trakt.tv e printa no console");
print("----------------------------------------------------------------------");

for movie in movies:
  title = movie.find("div", "titles");
  rating = movie.find("div", "percentage").text;
  watching = title.select_one("h4").text;
  actual_title = title.select_one("h3").text;
  print(f"\"{actual_title}\" currently has {watching} and a rating of {rating}");