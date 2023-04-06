import requests 

api_key = input('API key를 입력하세요: ')
video_id = input('Youtube Video ID를 입력하세요: ')

url = f"https://www.googleapis.com/youtube/v3/videos?id={video_id}&key={api_key}&part=snippet,statistics"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()["items"][0]["snippet"]
    title = data["title"]
    channel_title = data["channelTitle"]
    description = data["description"]
    view_count = response.json()["items"][0]["statistics"]["viewCount"]

    print(f"영상제목: {title}")
    print('------------------------------------------------------------')
    print(f"채널명: {channel_title}")
    print('------------------------------------------------------------')
    print(f"영상설명: {description}")
    print('------------------------------------------------------------')
    print(f"조회수: {view_count}")
    print('------------------------------------------------------------')
else:
    print("Error: Unable to retrieve video information.")


from PyKomoran import *

komoran = Komoran("STABLE")
url = f"https://www.googleapis.com/youtube/v3/commentThreads?key={api_key}&textFormat=plainText&part=snippet&videoId={video_id}&maxResults=100"
nouns = list()
response = requests.get(url)

if response.status_code == 200:
    data = response.json()["items"]
    for comment in data:
        text = comment["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
        nouns += [noun for noun in komoran.nouns(text)]
else:
    print("Error: Unable to retrieve comments.")


import numpy as np
from PIL import Image
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter

# Load the banner image
banner_mask = np.array(Image.open('BE-Team-1/youtube1.png'))

# for views
text = ' '.join(nouns)
wordcloud = WordCloud(font_path='C:\Windows\Fonts\malgun.ttf', mask=banner_mask, width=800, height=800, background_color='white', min_font_size=10).generate(text)

plt.figure(figsize=(8,8))
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=0)
plt.show()

# Generate the word cloud
word_counts = Counter(nouns)
wordcloud = WordCloud(font_path='C:\Windows\Fonts\malgun.ttf', background_color='white', min_font_size=10, mask=banner_mask, contour_width=2, contour_color='black', width=800, height=400).generate_from_frequencies(word_counts)

# Save the word cloud to a file
wordcloud.to_file("wordcloud_banner.png")
