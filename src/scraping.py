from openai import OpenAI
import requests
from bs4 import BeautifulSoup
import settings

url = "https://www.apple.com/jp/macbook-pro/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

text_nodes = soup.find_all("div")
text_all = []
for t in text_nodes:
    text_all.append(t.text.replace("\t", "").replace("\n", ""))
fine_text = "".join(text_all)
print(fine_text)