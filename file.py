from urllib.request import urlopen
import re

print("Python practice for web scraping")

url = "http://olympus.realpython.org/profiles/poseidon"
page = urlopen(url)
page

html_bytes = page.read()
html = html_bytes.decode("utf-8")

# print(html)

title_index = html.find("<title>")
# 14

match_results = re.search("ab*c", "ABC", re.IGNORECASE)
match_results.group()

print(match_results)