import requests
from bs4 import BeautifulSoup
import lxml
import json
# youtube_url = "https://www.codewithharry.com/videos/"
# response = requests.request("GET", youtube_url)
# print(response)
# soup = BeautifulSoup(response.text, "lxml")
#
#
# p =soup.find(class_='p-4 md:w-1/3 flex justify-center')
# # print(p.prettify())
# print(p.text)
# print(p.span)

# Send a GET request to the target URL
url = "https://www.codewithharry.com/videos/"
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find all the video titles on the page
video_titles = soup.find_all("h2", class_="video-card-title")

# Print the video titles
for title in video_titles:
    print(title.text.strip())